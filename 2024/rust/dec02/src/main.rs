use dec02::{load_input, part1, part2};


fn main() {
    let lines = load_input("./src/input.txt").expect("File doesn't exist");

    let test = "7 6 4 2 1
                1 2 7 8 9
                9 7 6 2 1
                1 3 2 4 5
                8 6 4 4 1
                1 3 6 7 9";
    let test1 = part1(&test);
    println!("test 1 : {:?}", test1);

    let answer1 = part1(&lines);
    println!("answer 1 : {:?}", answer1);

    let test2 = part2(&test);
    println!("test 2 : {:?}", test2);

    let answer2 = part2(&lines);
    println!("answer 2 : {:?}", answer2);
}
