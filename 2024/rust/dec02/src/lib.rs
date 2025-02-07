use std::fs;
use std::error::Error;


fn check_sequence(v: &Vec<i32>) -> bool {
    let increasing = v[0] < v[1];
 
    if increasing {
        if v.windows(2).all(|w| w[0] < w[1]) {
            return v.windows(2).all(|w| (w[1] - w[0]).abs() <= 3);
        }
        false
    }

    else {
        if v.windows(2).all(|w| w[0] > w[1]) {
            return v.windows(2).all(|w| (w[1] - w[0]).abs() <= 3);
        }
        false
    }
}

pub fn part1(input: &str) -> u32 {
    let reports: Vec<Vec<i32>> = input.lines()
        .map(|line| 
            line.split_whitespace()
            .filter_map(|n| n.parse().ok())
            .collect())
        .collect();

    let mut safe = 0;
    for report in reports.iter() {

        if check_sequence(&report){
            safe += 1
        }
    }
    safe
}


pub fn part2(input: &str) -> u32 {
    
    let reports: Vec<Vec<i32>> = input.lines()
        .map(|line| 
            line.split_whitespace()
            .filter_map(|n| n.parse().ok())
            .collect())
        .collect();

    let mut safe = 0;
    'reportloop: for report in reports.iter() {
        for i in 0..report.len() {
            let mut new_report: Vec<i32> = report.clone();
            new_report.remove(i);
            if check_sequence(&new_report){
                safe += 1;
                continue 'reportloop;
            }

        }
    }
    safe
}

pub fn load_input(path: &str) -> Result<String, Box<dyn Error>> {
    let message: String = fs::read_to_string(path)?;
    Ok(message)
}
