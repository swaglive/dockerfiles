workflow "Push" {
  on = "push"
  resolves = ["Build Docker Image"]
}

action "Build Docker Image" {
  uses = "actions/docker/cli@86ff551d26008267bb89ac11198ba7f1d807b699"
  args = "build -f thumbor/6.6.0/Dockerfile ."
}
