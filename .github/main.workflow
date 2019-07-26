workflow "Push" {
  on = "push"
  resolves = ["Docker - Login"]
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
