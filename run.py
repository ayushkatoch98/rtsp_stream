import subprocess
import threading
import logic
import time

THREAD_HOLDER = []



t = logic.Streaming("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4" , "myvid.m3u8" , hideLogs=True)
t.run()
t2 = logic.Streaming("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4" , "yourvid.m3u8" , hideLogs=True)
t2.run()

times = 100

while(t.isRunning()):
    time.sleep(20)

    if times == 0:
        t.stop()

    times -= 1