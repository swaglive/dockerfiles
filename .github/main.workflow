workflow "New workflow" {
  on = "push"
  resolves = ["Build Docker image"]
}

action "Build Docker image" {
  uses = "actions/docker/cli@master"
  args = ["build", "-f", "thumbor/6.6.0/Dockerfile", "."]
}
