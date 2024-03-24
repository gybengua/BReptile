import os
import subprocess


class AriaServer:
    ListenPort = None

    @classmethod
    def StartServer(cls, config):
        cls.ListenPort      = config.ListenPort
        ariaDir             = "/aria/"
        sessionFile         = ariaDir + "aria.session"
        logFile             = ariaDir + "aria.log"
        saveSessionInterval = 30

        if not os.path.exists(ariaDir):
            os.makedirs(ariaDir)

        if not os.path.exists(sessionFile):
            with open(sessionFile, "wb"):
                pass


        headers = ""
        for header in config.Headers:
            headers = headers +  f"--header=\"{header}\" "

        cls.ExcuteProcess(r"C:\Users\admin\Desktop\BReptile\aria2c.exe",
                          f"--enable-rpc --rpc-listen-all=true --rpc-allow-origin-all=true " +
                          f"--rpc-listen-port={config.ListenPort} " +
                          f"--rpc-secret={config.Token} " +
                          f"--input-file=\"{sessionFile}\" --save-session=\"{sessionFile}\" " +
                          f"--save-session-interval={saveSessionInterval} " +
                          f"--log=\"{logFile}\" --log-level={config.LogLevel.name.lower()} " +
                          f"--max-concurrent-downloads={config.MaxConcurrentDownloads} " +
                          f"--max-connection-per-server={config.MaxConnectionPerServer} " +
                          f"--split={config.Split} " +
                          f"--min-split-size={config.MinSplitSize}M " +
                          f"--max-overall-download-limit={config.MaxOverallDownloadLimit} " +
                          f"--max-download-limit={config.MaxDownloadLimit} " +
                          f"--max-overall-upload-limit={config.MaxOverallUploadLimit} " +
                          f"--max-upload-limit={config.MaxUploadLimit} " +
                          f"--continue={str(config.ContinueDownload).lower()} " +
                          f"--allow-overwrite=true " +
                          f"--auto-file-renaming=false " +
                          f"--file-allocation={config.FileAllocation.name.lower()} " +
                          f"{headers}" +
                          "")

    @classmethod
    def ExcuteProcess(cls, exe, arg):
        subprocess.run(exe + " " + arg)
