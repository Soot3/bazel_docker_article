workspace(
    # Naming your workspace can help you reference it elsewhere, in other workspaces or projects 
    name = "bazel_docker_test",
)

## Download the Bazel repository (rules_docker) as a compressed archive file, decompresses it, and makes its targets or functions available for binding.

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "b1e80761a8a8243d03ebca8845e9cc1ba6c82ce7c5179ce2b295cd36f7e394bf",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.25.0/rules_docker-v0.25.0.tar.gz"]
)

### Docker Setup: loading the archived repository as well as its dependencies

load("@io_bazel_rules_docker//repositories:repositories.bzl", container_repositories = "repositories")

container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

## loading a specific function from the rules_docker repository, the container_pull function

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull"
)
container_pull(
  name = "flask_base",
  registry = "index.docker.io",
  repository = "sootersaalu/flask_base",
  tag = "v.0.1"
)

