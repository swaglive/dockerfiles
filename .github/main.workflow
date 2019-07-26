workflow "Push" {
  on = "push"
  resolves = [
    "Run Echo"
  ]
}

action "Run Echo" {
  uses = "./"
  args = "echo push or "
}
