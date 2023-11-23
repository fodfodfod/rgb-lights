use std::cmp::Ordering;
use std::thread;
use std::time;
use gpio::GpioOut;
use gpio::sysfs::SysFsGpioOutput;
use unbothered_gpio::UnbotheredGpioPinWriter;

static RED_PORT: u16 = 7;
static GREEN_PORT: u16 = 29;
static BLUE_PORT: u16 = 31;
static TIME_CONSTANT: u64 = 1000;


fn main() {
    println!("Hello, world!");

    let mut values: Color = Color::new();
    let mut red_pin = gpio::sysfs::SysFsGpioOutput::open(RED_PORT).unwrap();
    let mut green_pin = gpio::sysfs::SysFsGpioOutput::open(GREEN_PORT).unwrap();
    let mut blue_pin = gpio::sysfs::SysFsGpioOutput::open(BLUE_PORT).unwrap();
    println!("hi again");
    loop{
        values.rainbow_cycle();
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
    }
}

fn controller(color: &Color, red_pin: &mut SysFsGpioOutput, green_pin: &mut SysFsGpioOutput, blue_pin: &mut SysFsGpioOutput){
    let red_port_number = RED_PORT;
    let green_port_number = GREEN_PORT;
    let blue_port_number = BLUE_PORT;


    red_pin.set_high();
    green_pin.set_high();
    blue_pin.set_high();
    let mut list = color.convert_to_list(); 
    list.sort();
    let mut final_wait_time = 255;
    

    let wait_time = list.get(0).unwrap().intensity - list.get(1).unwrap().intensity - list.get(2).unwrap().intensity;
    final_wait_time -= wait_time;
    thread::sleep(time::Duration::from_millis(wait_time as u64/TIME_CONSTANT)); 
    match list.get(0).unwrap().port{
        red_port_number => red_pin.set_low(),
        green_port_number => green_pin.set_low(),
        blue_port_number => blue_pin.set_low(),
    }; 
    
    list.remove(0);
    let wait_time = list.get(0).unwrap().intensity - list.get(1).unwrap().intensity;
    final_wait_time -= wait_time;
    thread::sleep(time::Duration::from_millis(wait_time as u64/TIME_CONSTANT)); 
    match list.get(0).unwrap().port{
        red_port_number => red_pin.set_low(),
        green_port_number => green_pin.set_low(),
        blue_port_number => blue_pin.set_low(),
    }; 
    
    list.remove(0);
    let wait_time = list.get(0).unwrap().intensity;
    final_wait_time -= wait_time;
    thread::sleep(time::Duration::from_millis(wait_time as u64/TIME_CONSTANT)); 
    
    match list.get(0).unwrap().port{
        red_port_number => red_pin.set_low(),
        green_port_number => green_pin.set_low(),
        blue_port_number => blue_pin.set_low(),
    }; 
    let wait_time = final_wait_time;
    thread::sleep(time::Duration::from_millis(wait_time as u64/TIME_CONSTANT)); 
    //
    //find next color
}
#[derive(Copy)]
#[derive(Clone)]
struct LED{
    intensity: u8,
    port: u16
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
        Color { red: LED{ intensity: 255, port: RED_PORT}, green: LED{ intensity: 0, port: GREEN_PORT}, blue: LED { intensity: 0, port: BLUE_PORT}}
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
    pub fn convert_to_list(&self) -> Vec<LED>{
        let list = vec![self.red, self.green, self.blue];
        list
    }
}
