use std::fs;
use std::error::Error;


pub fn part1(input: &str) -> u32 {
    // Create two vecs for numbers on either side
    let (mut left, mut right): (Vec<u32>, Vec<u32>) = input.lines()
        .map(|line| {
            let n: Vec<u32> = line 
                .split_whitespace()
                .map(|n| n.parse().ok().unwrap())
                .collect();
            (n[0], n[1])
        })
        .unzip();

    // sort them
    left.sort();
    right.sort();

    // iter over both and get the abs_diff, then sum everything
    left.iter()
        .zip(right)
        .map(|(l, r)| l.abs_diff(r))
        .sum()
}

pub fn part2(input: &str) -> u32 {
    // Create two vecs for numbers on either side
    let (left, right): (Vec<u32>, Vec<u32>) = input.lines()
        .map(|line| {
            let n: Vec<u32> = line 
                .split_whitespace()
                .map(|n| n.parse().ok().unwrap())
                .collect();
            (n[0], n[1])
        })
        .unzip();

    // get the count of each left num in the right column 
    left.iter()
        .map(|n| {
            let multi = right.iter()
            .filter(|&m| *m == *n )
            .count() as u32;
            n * multi
        })
        .sum()
}

pub fn load_input(path: &str) -> Result<String, Box<dyn Error>> {
    let message: String = fs::read_to_string(path)?;
    Ok(message)
}
