import subprocess
import threading
import platform
import os
import uuid

class Streaming():

    def __init__(self , url: str , file_path: str , hideLogs: bool = False):
        threading.Thread.__init__(self)
        self.url = url
        self.filePath = file_path
        self.id = str(uuid.uuid4())

        if hideLogs:
            self.logging = "-loglevel quiet"
        else:
            self.logging = ""

    def run(self):
        print("Running Thread " + self.id)

        command = "ffmpeg {logging} -rtsp_transport tcp -i {url} -hls_time 2 -y {filePath}".format(logging = self.logging , url = self.url , filePath = self.filePath)

        self.sp = subprocess.Popen(command , shell=True)
             
    def isRunning(self):
        if self.sp.poll() is None:
            return True
        return False

    def stop(self):

        if platform.system().lower() == "windows":
            subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid = self.sp.pid))
        else:
            os.system("kill -9 %s"%self.sp.pid)