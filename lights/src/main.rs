use std::cmp::Ordering;
static red_port: i32 = 7;
static green_port: i32 = 29;
static blue_port: i32 = 31;
fn main() {
    println!("Hello, world!");

    let mut values: Color = Color::new();
    
    //tokio::spawn(async{ controller(&values)});

    loop{
        values.rainbow_cycle();
        //values.print_color();
    }
    //find_next_color(&mut values);
}

fn controller(color: &Color){
    //turn on everything
    let mut list = color.convert_to_list(); 
    list.sort();
    let mut final_wait_time = 255;
    

    let wait_time = list.get(0).unwrap().intensity - list.get(1).unwrap().intensity - list.get(2).unwrap().intensity;
    final_wait_time -= wait_time;
    list.remove(0);
    
    //turn off
    let wait_time = list.get(0).unwrap().intensity - list.get(1).unwrap().intensity;
    final_wait_time -= wait_time;
    list.remove(0);
    //turn off
    let wait_time = list.get(0).unwrap().intensity;
    final_wait_time -= wait_time;
    //turn off
    let wait_time = final_wait_time;
    //
    //find next color
}
#[derive(Copy)]
#[derive(Clone)]
struct LED{
    intensity: u8,
    port: i32
}

impl Ord for LED{
    fn cmp(&self, other: &Self) -> Ordering{
        (self.intensity).cmp(&other.intensity)
    }
}
impl PartialOrd for LED{
    fn partial_cmp(&self, other: &Self) -> Option<Ordering>{
        Some(self.cmp(other))
    }
}
impl PartialEq for LED{
    fn eq(&self, other: &Self) -> bool {
        self.intensity == other.intensity
    }
}
impl Eq for LED { }

struct Color{
    red: LED,
    green: LED,
    blue: LED,
}

impl Color{
    fn new() -> Self {
        Color { red: LED{ intensity: 255, port: red_port}, green: LED{ intensity: 0, port: green_port}, blue: LED { intensity: 0, port: blue_port}}
    }
    pub fn rainbow_cycle(&mut self) {
        if self.red.intensity == 255 && self.green.intensity < 255 && self.blue.intensity == 0 {
            self.green.intensity += 1;
        }
        if self.red.intensity > 0 && self.green.intensity == 255 && self.blue.intensity == 0 {
            self.red.intensity -= 1;
        }
        if self.red.intensity == 0 && self.green.intensity == 255 && self.blue.intensity < 255 {
            self.blue.intensity += 1;
        }
        if self.red.intensity == 0 && self.green.intensity > 0 && self.blue.intensity == 255 {
            self.green.intensity -= 1;
        }
        if self.red.intensity < 255 && self.green.intensity == 0 && self.blue.intensity == 255 {
            self.red.intensity += 1;
        }
        if self.red.intensity == 255 && self.green.intensity == 0 && self.blue.intensity > 0 {
            self.blue.intensity -= 1;
        }
    }
    pub fn print_color(&self) {
        //println!("Red: {}\nGreen: {}\nBlue: {}\n", self.red, self.green, self.blue);
    }
    pub fn convert_to_list(&self) -> Vec<LED>{
        let list = vec![self.red, self.green, self.blue];
        return list;
    }
}
