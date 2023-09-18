# #!/usr/bin/env python3

# import rospy
# from controller_manager_msgs.srv import LoadController

# def load_controller(controller_name):
#     rospy.wait_for_service('/controller_arm/controller_manager/load_controller')
#     try:
#         load_controller_service = rospy.ServiceProxy('/controller_arm/controller_manager/load_controller', LoadController)
#         response = load_controller_service(controller_name)
#         return response.ok
#     except rospy.ServiceException as e:
#         rospy.logerr("Service call failed: %s", str(e))
#         return False

# if __name__ == '__main__':
#     rospy.init_node('load_controller_example')
    
#     # Replace 'joint1_position_controller' and 'joint2_position_controller' with your desired controller names
#     controller1_loaded = load_controller('joint1_position_controller')
#     controller2_loaded = load_controller('joint2_position_controller')
    
#     if controller1_loaded and controller2_loaded:
#         rospy.loginfo("Controllers loaded successfully")
#     else:
#         rospy.logerr("Failed to load controllers")
