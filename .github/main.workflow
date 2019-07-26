workflow "Push" {
  on = "push"
  resolves = ["Build Docker Image"]
}

action "Build Docker Image" {
  uses = "actions/docker/cli@master"
  args = ["build", "-t", "swaglive/thumbor:6.6.0", "thumbor/6.6.0"]
}
