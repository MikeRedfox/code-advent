use crate::days::utils::get_data;

#[allow(unused)]
pub fn part1(filepath: &str) -> i32 {
    let data = get_data(filepath);
    let mut wheel = 50;
    let mut step = 0;
    let mut s = 0;
    for istruzione in data {
        let direzione = &istruzione[..1];
        match direzione {
            "L" => step = -istruzione[1..].parse::<i32>().unwrap(),
            "R" => step = istruzione[1..].parse::<i32>().unwrap(),
            _ => panic!("aaaaaaaaaaaaaaaaaaah"),
        }
        wheel = (wheel + step) % 100;
        if wheel < 0 {
            wheel = 100 + wheel
        } else if wheel == 0 {
            s += 1
        }
        // println!("{}\t{}", step, wheel);
    }
    s
}
#[allow(unused)]
pub fn part2(filepath: &str) -> i32 {
    let data = get_data(filepath);
    let mut wheel = 50;
    let mut step = 0;
    let mut s = 0;
    for istruzione in data {
        let direzione = &istruzione[..1];
        match direzione {
            "L" => step = -istruzione[1..].parse::<i32>().unwrap(),
            "R" => step = istruzione[1..].parse::<i32>().unwrap(),
            _ => panic!("aaaaaaaaaaaaaaaaaaah"),
        }
        for _ in 0..step.abs() {
            if step > 0 {
                wheel = (wheel + 1) % 100;
            }
            if step < 0 {
                wheel = wheel - 1;
            }
            if wheel < 0 {
                wheel = 100 - 1
            } else if wheel == 0 {
                s += 1
            }
        }
        // println!("{}\t{}", step, wheel);
    }
    s
}
