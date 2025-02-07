use std::fs;
use std::error::Error;


pub fn part1(input: &str) -> u32 {
    // Create two vecs for numbers on either side
    let reports: Vec<Vec<i32>> = input.lines()
        .map(|line| 
            line.split_whitespace()
            .filter_map(|n| n.parse().ok())
            .collect())
        .collect();

    // iter over report, make sure num and next_num are within 3, make sure we are either
    // continuosly increasing or decreasing
    // Maybe have some helper functions and then use a filter
    // So filter out ones that aren't strictly increasing or decreasing (return true/false)
    // then filter out ones that have abs diffs of >3 between numbers (also return true false)
    let mut safe = 0;
    'outer: for report in reports.iter() {

        let (mut m, mut n) = (0, 1);
        if report[m] == report [n] {
            continue; 
        }
        let increasing = report[m] < report[n];
        match increasing {

            true => {

                while n < report.len() {
                    if ((report[n] - report[m]).abs() > 3) || ((report[n] - report[m]).abs() < 1 || report[n] < report[m] ){
                        continue 'outer;
                    }
                    m += 1;
                    n += 1;
                }
                safe += 1;
            },
            false => {
                while n < report.len() {
                    if ((report[m] - report[n]).abs() > 3) || ((report[m] - report[n]).abs() < 1) || report[n] > report[m] {
                        continue 'outer;
                    }
                    m += 1;
                    n += 1;
                }
                safe += 1;
            },
        }
    }
    safe
}


pub fn part2(input: &str) -> u32 {
    1
}

pub fn load_input(path: &str) -> Result<String, Box<dyn Error>> {
    let message: String = fs::read_to_string(path)?;
    Ok(message)
}
