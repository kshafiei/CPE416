import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
from sensor_msgs.msg import LaserScan

class Roomba(Node):

    def __init__(self):
        super().__init__('roomba')
        
        self.publisher_ = self.create_publisher(TwistStamped, 'cmd_vel', 10)

        # Functions running at 1Hz
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.subscription = self.create_subscription(
                LaserScan,
                '/scan',
                self.listener_callback,
                10)

        self.state = 0 # 0 - forward, 1 - reverse, 2 - turning

        self.forward_msg = TwistStamped()
        self.forward_msg.twist.linear.x = 0.45

        self.reverse_msg = TwistStamped()
        self.reverse_msg.twist.linear.x = -0.45

        self.turn_msg = TwistStamped()
        self.turn_msg.twist.angular.z = 0.2

        self.n = 0

    # Callback for the events
    def timer_callback(self):
        
        if (self.state == 0):
            self.get_logger().info('Robot is moving forward!')
            self.publisher_.publish(self.forward_msg) 
        elif (self.state == 1):
            self.get_logger().info('Robot is reversing!')
            self.publisher_.publish(self.reverse_msg)
            self.n += 1

            if (self.n >= 9):
                self.state = 2
                self.n = 0
        else:
            self.get_logger().info('Robot is turning!')
            self.publisher_.publish(self.turn_msg)        

    def listener_callback(self, msg):
        ranges = msg.ranges
        first = ranges[:90]
        last = ranges[-90:]
        part = first + last
        avgs = [0 for i in range(6)]
        turn = 0

        if (self.state == 0):
            for i in range(6):
                avgs[i] = self.get_avg(part[i*30:i*30+30])
                if (avgs[i] < 0.83):
                    turn = 1
                    break
        elif (self.state == 2):
            for i in range(6):
                avgs[i] = self.get_avg(part[i*30:i*30+30])
                if (avgs[i] < 1.5):
                    turn = 1
                    break

        print(avgs)

        if(self.state == 0 and turn):
            self.state = 1
        elif(self.state == 2 and not turn):
            self.state = 0

    def get_avg(self, values):   
        total = 0
        valids = 0

        for i in range(len(values)):
            if values[i] < 20:
                total += values[i]
                valids += 1
        if valids != 0:
            average = total/valids
        else:
            average = 0

        return average

def main(args=None):
    rclpy.init(args=args)

    roomba = Roomba()
    rclpy.spin(roomba)

    roomba.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
