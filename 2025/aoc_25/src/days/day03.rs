use crate::days::utils::get_data;

#[allow(unused)]
pub fn part1(filepath: &str) -> i32 {
    let data = get_data(filepath);
    let mut s = 0;
    let mut maximum = 0;
    for line in data {
        maximum = 0;
        // println!("{}", line);
        for i in 0..line.len() - 1 {
            for j in i + 1..line.len() {
                let comb: String = vec![line.chars().nth(i).unwrap(), line.chars().nth(j).unwrap()]
                    .iter()
                    .collect();
                // println!("{}", comb);
                let n = comb.parse::<i32>().unwrap();
                if n > maximum {
                    maximum = n;
                }
            }
        }
        // println!("{}", maximum);
        s += maximum;
    }
    s
}
#[allow(unused)]
fn max_subsequence(s: &str, k: usize) -> String {
    let digits: Vec<u8> = s.bytes().collect();
    let n = digits.len();
    let to_remove = n - k;
    let mut remaining = to_remove;
    let mut stack: Vec<u8> = Vec::with_capacity(k);

    for &d in &digits {
        while let Some(&last) = stack.last() {
            if remaining > 0 && d > last {
                stack.pop();
                remaining -= 1;
            } else {
                break;
            }
        }
        stack.push(d);
    }

    let result = &stack[..k];

    String::from_utf8(result.to_vec()).unwrap()
}

#[allow(unused)]
pub fn part2(filepath: &str) -> i64 {
    let data = get_data(filepath);
    let mut s: i64 = 0;
    let mut maximum: i64 = 0;
    for line in data {
        maximum = 0;
        // println!("{}", line);
        s += max_subsequence(&line, 12).parse::<i64>().unwrap();
        // println!("{}", maximum);
    }
    // println!("{}", s);
    s
}
