The goal of this Docker image is to customize thumbor for performance.  Compatibility is not a concern.

# Notes
* Python 3.6 (thumbor is incompatible with 3.7 due to `async` reserved keyword)
* Includes all storage plugins
* Replaced `pillow` with `pillow-simd`
  * ~Compiled for AVX2~
  * Use default SSE4 (for blur support)
* Replaced `json` with `rapidjson` with `number_mode=NM_NATIVE` and `ensure_ascii=False`
* dockerize for config instead of `use-environment`
* Assumption of running in Kubernetes and therefore Will not provide a multi-process
