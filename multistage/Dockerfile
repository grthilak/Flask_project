FROM golang:1.8

WORKDIR /go/src/app
copy main.go .

RUN GOOS=linux go build -a -installsuffix cgo -o webserver .

CMD ["./webserver"]
