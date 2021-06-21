package main

import (
  "fmt"
  "log"
  "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "Hello world from go")
}

func main() {
  http.HandleFunc("/", handler)
  log.Fatal(http.ListenAndServe("0.0.0.0:8080", nil))
}
