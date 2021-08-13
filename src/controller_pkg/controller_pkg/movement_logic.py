from geometry_msgs.msg import Twist

def calculate_movement(controller):
    """
    This method causes the robot to follow the boundary of a wall.
    """
    # Create a geometry_msgs/Twist message
    msg = Twist()
    msg.linear.x = 0.0
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = 0.0

    # Logic for following the wall
    # >d means no wall detected by that laser beam
    # <d means an wall was detected by that laser beam
    d = controller.dist_thresh_wf
     
    if controller.leftfront_dist > d and controller.front_dist > d and controller.rightfront_dist > d:
        controller.wall_following_state = "search for wall"
        msg.linear.x = controller.forward_speed
        msg.angular.z = -controller.turning_speed_wf_slow # turn right to find wall

    elif controller.leftfront_dist > d and controller.front_dist < d and controller.rightfront_dist > d:
        controller.wall_following_state = "turn left"
        msg.angular.z = controller.turning_speed_wf_fast

    elif (controller.leftfront_dist > d and controller.front_dist > d and controller.rightfront_dist < d):
        if (controller.rightfront_dist < controller.dist_too_close_to_wall):
            # Getting too close to the wall
            controller.wall_following_state = "turn left"
            msg.linear.x = controller.forward_speed
            msg.angular.z = controller.turning_speed_wf_fast
        else:
            # Go straight ahead
            controller.wall_following_state = "follow wall"
            msg.linear.x = controller.forward_speed

    elif controller.leftfront_dist < d and controller.front_dist > d and controller.rightfront_dist > d:
        controller.wall_following_state = "search for wall"
        msg.linear.x = controller.forward_speed
        msg.angular.z = -controller.turning_speed_wf_slow # turn right to find wall

    elif controller.leftfront_dist > d and controller.front_dist < d and controller.rightfront_dist < d:
        controller.wall_following_state = "turn left"
        msg.angular.z = controller.turning_speed_wf_fast

    elif controller.leftfront_dist < d and controller.front_dist < d and controller.rightfront_dist > d:
        controller.wall_following_state = "turn left"
        msg.angular.z = controller.turning_speed_wf_fast

    elif controller.leftfront_dist < d and controller.front_dist < d and controller.rightfront_dist < d:
        controller.wall_following_state = "turn left"
        msg.angular.z = controller.turning_speed_wf_fast
                     
    elif controller.leftfront_dist < d and controller.front_dist > d and controller.rightfront_dist < d:
        controller.wall_following_state = "search for wall"
        msg.linear.x = controller.forward_speed
        msg.angular.z = -controller.turning_speed_wf_slow # turn right to find wall
     
    return msg