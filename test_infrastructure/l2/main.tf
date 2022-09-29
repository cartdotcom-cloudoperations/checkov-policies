# Dummy resources pulled from this guide:
# https://cloud.google.com/cdn/docs/setting-up-cdn-with-bucket#terraform

# Cloud Storage bucket
resource "random_id" "bucket_prefix" {
  byte_length = 8
}

resource "google_storage_bucket" "default" {
  name                        = "${random_id.bucket_prefix.hex}-my-bucket"
  location                    = "us-east1"
  uniform_bucket_level_access = true
  storage_class               = "STANDARD"
  force_destroy               = true
  website {
    main_page_suffix = "index.html"
    not_found_page   = "404.html"
  }
}

resource "google_storage_bucket_iam_member" "default" {
  bucket = google_storage_bucket.default.name
  role   = "roles/storage.objectViewer"
  member = "allUsers"
}

resource "google_compute_global_address" "default" {
  name = "example-ip"
}

resource "google_compute_backend_bucket" "default" {
  name        = "cat-backend-bucket"
  description = "Contains beautiful images"
  bucket_name = google_storage_bucket.default.name
  enable_cdn  = true
  cdn_policy {
    cache_mode        = "CACHE_ALL_STATIC"
    client_ttl        = 3600
    default_ttl       = 3600
    max_ttl           = 86400
    negative_caching  = true
    serve_while_stale = 86400
  }
}

resource "google_compute_url_map" "default" {
  name            = "http-lb"
  default_service = google_compute_backend_bucket.default.id
}

resource "google_compute_target_http_proxy" "default" {
  name    = "http-lb-proxy"
  url_map = google_compute_url_map.default.id
}

resource "google_compute_global_forwarding_rule" "default" {
  name                  = "http-lb-forwarding-rule"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL"
  port_range            = "80"
  target                = google_compute_target_http_proxy.default.id
  ip_address            = google_compute_global_address.default.id
}
