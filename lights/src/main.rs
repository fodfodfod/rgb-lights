#[tokio::main]
async fn main() {
    println!("Hello, world!");
    let red_port = 7;
    let green_port = 29;
    let blue_port = 31;

    let mut values: Color = Color {red: 0, green: 0, blue: 0};

    controller(&mut values).await;

    values.red = 255;
}

async fn controller(color: &mut Color){
    //turn on everything
    //wait for the greatest time
    //turn off
    //repeat
    //
    //find next color
}

fn find_next_color(current_color: &mut Color){

}

struct Color{
    red: i32,
    green: i32,
    blue: i32,
}
