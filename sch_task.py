class sch_task:
    def __init__(self , exec_time , m_type , args):

        self.exec_time  = exec_time
        self.m_type = m_type
        self.args = args

    def get_exec_time(self):
        return self.exec_time
    def reset_task(self , new_exec_time):
        self.exec_time = new_exec_time
    def execute(self ,all_nodes , current_time ):
        if self.m_type == "queue_message":
            if len(self.args)>2:
                all_nodes[self.args[0]].queue_message(self.args[1] , current_time , self.args[2] , self.args[3]) 
            else:
                all_nodes[self.args[0]].queue_message(self.args[1] , current_time)
        if self.m_type == "delete_node":
            del all_nodes[self.args[0]]
        if self.m_type == "flush_queue":
            all_nodes[self.args[0]].transmit_buffer = []
        if self.m_type == "show_recieved":
            all_nodes[self.args[0]].print_packets()
        if self.m_type == "send_beacon":
            all_nodes[self.args[0]].send_beacon(current_time)
        if self.m_type == "transmit_pending":
            #only a filler to stop early termination for independant tasks
            return 
        if self.m_type == "grant_transmit_permit":
            all_nodes[self.args[0]].permit_transmit(current_time , 5)
        if self.m_type == "remove_transmit_permit":
            all_nodes[self.args[0]].remove_permit()
        if self.m_type == "check_ack":
            all_nodes[self.args[0]].check_ack_initialize(current_time)
        if self.m_type == "LBS":
            all_nodes[self.args[0]].continuous_LBS(current_time , self.args[1])
        if self.m_type == "check_msg_ack":
            all_nodes[self.args[0]].check_ack_msg(current_time)
        
        
# more events should be handled 