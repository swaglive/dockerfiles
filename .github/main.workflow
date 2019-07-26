workflow "New workflow" {
  on = "push"
  resolves = ["GitHub Action for Docker"]
}

action "GitHub Action for Docker" {
  uses = "actions/docker/cli@master"
  args = ["build", "-f", "thumbor/6.6.0/Dockerfile", "."]
}
