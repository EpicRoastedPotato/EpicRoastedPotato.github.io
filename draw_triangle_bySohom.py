#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
from math import radians
#Setting pi
PI= 3.14159265359

class DrawTriangleNode(Node):

    def __init__(self):
        super().__init__("draw_triangle")
        #Topic where it is to be published
        self.cmd_vel_pub_=self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        
        #Initializing parameters of the triangle/shape
        self.length=2.0
        self.number_sides=3
        self.angle= radians(120.0)
        
        #creating a timer so as to repeat the action
        self.timer_=self.create_timer((1), self.send_velocity_command)
        self.get_logger().info("Draw triangle node has been started")
        self.get_logger().info("Enter Ctrl+C to stop drawing triangles")


    
    def send_velocity_command(self):
            
            #Loop that repeats as many number of sides there are
            for i in range(self.number_sides):
                msg=Twist()
                
                msg.linear.x=self.length
                self.cmd_vel_pub_.publish(msg)
                time.sleep(2)
                #Sleep so as to length completes publishing

                #Setting msg.linear.x to zero otherwise, that value gets published
                #and forms a triangle with round edges             
                msg.angular.z=self.angle
                msg.linear.x=0.0
                self.cmd_vel_pub_.publish(msg)
                time.sleep(2)
                #Sleep for same reason as above
                
                


def main(args=None):
    rclpy.init(args=args)
    node= DrawTriangleNode()
    rclpy.spin(node)
    #Spin allows to run the Node again and again until Ctrl C is pressed
    rclpy.shutdown()