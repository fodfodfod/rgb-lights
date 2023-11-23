#[tokio::main]
async fn main() {
    println!("Hello, world!");
    let red_port = 7;
    let green_port = 29;
    let blue_port = 31;

    let mut values: Color = Color::new();
    
    //tokio::spawn(async{ controller(&values)});

    for _ in 0..500{
        values.rainbow_cycle();
        values.print_color();
    }
    //find_next_color(&mut values);
}

async fn controller(color: &Color){
    //turn on everything
    //wait for the greatest time
    //turn off
    //repeat
    //
    //find next color
}



struct Color{
    red: u8,
    green: u8,
    blue: u8,
}

impl Color{
    fn new() -> Self {
        Color { red: 255, green: 0, blue: 0}
    }
    pub fn rainbow_cycle(&mut self) {
        if self.red == 255 && self.green < 255 && self.blue == 0 {
            self.green += 1;
        }
        if self.red > 0 && self.green == 255 && self.blue == 0 {
            self.red -= 1;
        }
        if self.red == 0 && self.green == 255 && self.blue < 255 {
            self.blue += 1;
        }
        if self.red == 0 && self.green > 0 && self.blue == 255 {
            self.green -= 1;
        }
        if self.red < 255 && self.green == 0 && self.blue == 255 {
            self.red += 1;
        }
        if self.red == 255 && self.green == 0 && self.blue > 0 {
            self.blue -= 1;
        }
    }
    pub fn print_color(&self) {
        println!("Red: {}\nGreen: {}\nBlue: {}\n", self.red, self.green, self.blue);
    }
}
