package main

import "fmt"

type node struct{
	num int
	next *node
}

func isPrime(target int, prime *node)(bool){
	if target % prime.num == 0 {
		return false
	}
	if prime.next == nil{
		return true
	}
	return isPrime(target, prime.next)
}

func main(){
	primeList := new(node)
	primeList.num = 2
	test := 100 // typing in your range
	tmp := primeList
	for i:=2; i < test; i++{
		if isPrime(i, primeList){
			prime := new(node)
			prime.num = i
			tmp.next = prime
			tmp = prime
		}
	}
	for tmp = primeList; tmp != nil; tmp = tmp.next{
		fmt.Println(tmp.num)
	}
}
