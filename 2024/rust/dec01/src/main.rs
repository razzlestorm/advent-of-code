use dec01::{load_input, part1, part2};


fn main() {
    let lines = load_input("./src/input.txt").expect("File doesn't exist");
    let answer1 = part1(&lines);
    println!("answer 1 : {:?}", answer1);

    let answer2 = part2(&lines);
    println!("answer 2 : {:?}", answer2);
}
