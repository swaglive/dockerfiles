workflow "Build and Push Docker Image" {
  on = "push"
  resolves = ["Docker - Push Image"]
}

action "Docker - Build Image" {
  uses = "actions/docker/cli@master"
  args = ["build", "-t", "swaglive/thumbor:6.6.0", "thumbor/6.6.0"]
}

action "Docker - Login" {
  uses = "actions/docker/login@master"
  needs = ["Docker - Build Image"]
  secrets = ["DOCKER_USERNAME", "DOCKER_PASSWORD"]
}

action "Docker - Push Image" {
  uses = "actions/docker/cli@master"
  needs = ["Docker - Login"]
  args = ["push", "swaglive/thumbor:6.6.0"]
}
