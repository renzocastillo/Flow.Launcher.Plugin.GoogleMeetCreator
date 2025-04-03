# -*- coding: utf-8 -*-

import os
import sys
import webbrowser

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

from flowlauncher import FlowLauncher

class GoogleMeetCreator(FlowLauncher):
    def query(self, param):
        try:
            if not param:
                return [{
                    "Title": "Create Google Meet",
                    "SubTitle": "Press Enter to create a new meeting",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "create_meet",
                        "parameters": []
                    }
                }]
            
            return [{
                "Title": f"Create Google Meet: {param}",
                "SubTitle": "Press Enter to create a meeting with this title",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "create_meet",
                    "parameters": [param]
                }
            }]
        except Exception as e:
            return [{
                "Title": "Error",
                "SubTitle": f"Failed to process query: {str(e)}",
                "IcoPath": "Images/app.png"
            }]

    def create_meet(self, title=None):
        try:
            base_url = "https://meet.google.com/new"
            if title:
                # URL encode the title
                encoded_title = title.replace(" ", "+")
                url = f"{base_url}?title={encoded_title}"
            else:
                url = base_url
            
            # Open in browser
            webbrowser.open(url)
            
            return [{
                "Title": "Google Meet",
                "SubTitle": "Opening Google Meet in your browser...",
                "IcoPath": "Images/app.png"
            }]
        except Exception as e:
            return [{
                "Title": "Error",
                "SubTitle": f"Failed to create meeting: {str(e)}",
                "IcoPath": "Images/app.png"
            }]

if __name__ == "__main__":
    GoogleMeetCreator() 