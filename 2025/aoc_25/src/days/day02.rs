use crate::days::utils::get_data;

#[allow(unused)]
pub fn part1(filepath: &str) -> i64 {
    let binding = get_data(filepath);
    let data: Vec<&str> = binding[0].split(",").collect();
    let mut s = 0;
    for istruzione in data {
        let valori: Vec<&str> = istruzione.split("-").collect();
        // println!("{} ++ {}", valori[0], valori[1]);
        let l = valori[0].parse::<i64>().unwrap();
        let r = valori[1].parse::<i64>().unwrap();
        for n in l..r {
            let lun = n.to_string().len();
            let n_str = n.to_string();
            let half = lun / 2;
            if lun % 2 == 0 {
                if n_str[0..half] == n_str[half..] {
                    s += n
                }
            }
        }
    }
    s
}

pub fn part2(filepath: &str) -> i64 {
    let binding = get_data(filepath);
    let data: Vec<&str> = binding[0].split(",").collect();
    let mut ar: Vec<i64> = vec![];
    for istruzione in data {
        let valori: Vec<&str> = istruzione.split("-").collect();
        // println!("{} ++ {}", valori[0], valori[1]);
        let l = valori[0].parse::<i64>().unwrap();
        let r = valori[1].parse::<i64>().unwrap();
        for n in l..r {
            let lun = n.to_string().len();
            let n_str = n.to_string();
            let half = lun / 2;
            for j in 2..half + 1 {
                for k in 2..half + 1 {
                    if n_str[0..j].repeat(k) == n_str {
                        if !ar.contains(&n) {
                            ar.push(n);
                        }
                    }
                }
            }
            if lun % 2 == 0 {
                if n_str[0..half] == n_str[half..]
                    || n_str.chars().all(|c| c == n_str.chars().next().unwrap())
                {
                    if !ar.contains(&n) {
                        ar.push(n)
                    }
                }
            }
        }
    }
    ar.into_iter().sum()
}
