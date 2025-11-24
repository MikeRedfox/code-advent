package main

import "fmt"

func main() {
	t := [][]int{{3, 0, 0, -3, 2}, {-3, 3, 0, 0, 9}, {-1, 0, 4, 0, 1}, {0, 0, -2, 2, 8}}
	score := 0
	m := 0

	for i := 0; i < 100; i++ {
		for j := 0; j < 100-i; j++ {
			for k := 0; k < 100-i-j; k++ {
				h := 100 - i - j - k
				a := t[0][0]*i + t[1][0]*j + t[2][0]*k + t[3][0]*h
				b := t[0][1]*i + t[1][1]*j + t[2][1]*k + t[3][1]*h
				c := t[0][2]*i + t[1][2]*j + t[2][2]*k + t[3][2]*h
				d := t[0][3]*i + t[1][3]*j + t[2][3]*k + t[3][3]*h
				e := t[0][4]*i + t[1][4]*j + t[2][4]*k + t[3][4]*h

				if a <= 0 || b <= 0 || c <= 0 || d <= 0 {
					score = 0
					continue
				}
				if e != 500 {
					continue
				}
				score = a * b * c * d
				if score > m {
					m = score
				}
			}
		}
	}
	fmt.Println(m)

}
