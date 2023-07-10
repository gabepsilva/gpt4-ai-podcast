import json
import boto3
import pygame

from people.host import Host
from people.guest import Guest
from people.special_guest import SpecialGuest


class Podcast():
    def __init__(self):

        self.host = Host()
        self.guest = Guest()
        self.special_guest = SpecialGuest()

        host_context = self.get_host_context("./context/host.json")
        guest_context = self.get_guest_context("./context/guest.json")

        self.host.give_context(host_context)
        self.guest.give_context(guest_context)

        host_says = self.host.introduce_guest()
        self.transcript(host_says)
        self.broadcast("Matthew", host_says)

        while True:

            guest_says = self.guest.reply(host_says)
            self.transcript(guest_says)
            self.broadcast("Joanna", guest_says)

            host_says = self.host.reply(guest_says)
            self.transcript(host_says)
            self.broadcast("Matthew", host_says)

            user_input = input("Please enter something: ")
            if len(user_input) > 0:
                guest_says = self.guest.reply(user_input)
                self.transcript(guest_says)
                self.broadcast("Joanna", guest_says)

                host_says = self.host.reply(user_input)
                self.transcript(host_says)
                self.broadcast("Matthew", host_says)

    def transcript(self, msg):
        print(msg)
        print("--------------------------------")
        print("\n\n\n\n")

    def broadcast(self, voice: str, msg: str):
        polly_client = boto3.Session(
            region_name='us-east-1'  # choose the AWS region you are using
        ).client('polly')

        # Provide the text and the voice id (you can choose different voices)
        response = polly_client.synthesize_speech(
            Text=msg,
            OutputFormat='mp3',
            VoiceId=voice  # you can choose different voices, 'Joanna' is just an example
        )

        # The response contains the audio stream in the 'AudioStream' key
        with open('speech.mp3', 'wb') as file:
            file.write(response['AudioStream'].read())

        # Now, you can use pygame to play the audio file
        pygame.mixer.init()
        pygame.mixer.music.load('speech.mp3')
        pygame.mixer.music.play()

        # Keep the script running until the audio has finished playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def get_host_context(self, json_file_path: str) -> str:
        ctx = self.__loads_json__(json_file_path)
        return ctx['gpt_output']

    def get_guest_context(self, json_file_path: str) -> str:
        ctx = self.__loads_json__(json_file_path)
        return ctx['gpt_output']

    def __loads_json__(self, file_path: str) -> str:
        with open(file_path, 'r') as file:
            ret = json.load(file)
            return ret
