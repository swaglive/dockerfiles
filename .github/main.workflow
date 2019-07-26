workflow "Push" {
  on = "push"
  resolves = ["GitHub Action for Docker"]
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

action "GitHub Action for Docker" {
  uses = "actions/docker/cli@86ff551d26008267bb89ac11198ba7f1d807b699"
  needs = ["Docker - Login"]
  args = ["push", "swaglive/thumbor:6.6.0"]
}
