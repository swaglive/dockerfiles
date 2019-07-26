workflow "New workflow" {
  on = "push"
  resolves = ["Build Docker image"]
}

action "Build Docker image" {
  uses = "actions/docker/cli@86ff551d26008267bb89ac11198ba7f1d807b699"
  args = "build -f thumbor/6.6.0/Dockerfile .
}
