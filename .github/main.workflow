workflow "Push" {
  on = "push"
  resolves = ["Docker Registry"]
}

action "Build Docker Image" {
  uses = "actions/docker/cli@master"
  args = ["build", "-t", "swaglive/thumbor:6.6.0", "thumbor/6.6.0"]
}

action "Docker Registry" {
  uses = "actions/docker/login@86ff551d26008267bb89ac11198ba7f1d807b699"
  needs = ["Build Docker Image"]
  secrets = ["DOCKER_USERNAME", "DOCKER_PASSWORD"]
}
