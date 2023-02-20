## loading the needed functions from the rules_docker repository

load("@io_bazel_rules_docker//container:container.bzl", "container_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_push")

# container_image packages a new docker image, new layers can be added to a base image using its parameters

container_image(
    name = "my_app",
    base = "@flask_base//image",
    entrypoint = ["main.py"],
    files = [
        "main.py"
    ],
    ports = ["5000"],
)

# container_push pushes a local image to a registry of your choice (DockerHub, Google Registry, Gitlab registry or Github packages)

container_push(
    name = "publish",
    format = "Docker",
    image = ":my_app",
    registry = "index.docker.io",
    repository = "sootersaalu/bazel_docker_test",
    tag = "1",
)
