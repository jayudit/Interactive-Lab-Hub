

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.
3. (extra: Learn about what exactly Git is from [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).)

### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process
1. Video sketch of the prototyped interaction
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

\*\***Describe your setting, players, activity and goals here.**\*\*

Setting: For this lab, the setting is a bathroom. The idea for this device is a smart electric toothbrush that helps the player/user brush their teeth more effectively. My player, Anthony, has an 8 am class at Cornell Tech and he hates getting up early. Before going to class each morning, Anthony rushes to brush his teeth and almost always ends up rushing and not brushing for the recommended 2 minutes.

To avoid dental issues in the future, Anthony has decided to buy this state-of-the-art smart electric toothbrush. The activity for this interaction involves Anthony picking up the toothbrush and pressing the start button on the device when he starts brushing his teeth. The toothbrush flashes a red (warning light) every 30 seconds that indicates to the player to switch to another quadrant of their mouth. After 2 minutes are up, the toothbrush flashes a green light that notifies the player that they can stop brushing their teeth.

The goals for the player is to brush their teeth for the recommended two minutes spending 30 seconds in each quadrant of the mouth.

\*\***Include a picture of your storyboard here**\*\*

![storyboard](https://user-images.githubusercontent.com/70334332/132440683-735df2e6-4a32-4886-8d86-f70c8e5504de.jpg)

Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.

\*\***Summarize feedback you got here.**\*\*

I got feedback to keep the light on the whole time instead of using flashing lights. After each 30 seconds pass, the light can transition onto the next color.

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

\*\***Are there things that seemed better on paper than acted out?**\*\*

The physical interaction with my device felt pretty natural and smooth. I acted out brushing my teeth for the full two minutes while flashing the respective lights as mentioned on the storyboard. One thing I did notice though, is that the light has to flash for long enough so the person doesn't miss the light. 3 seconds might be too short because one might miss the flashing light. Therefore, the light must flash for at least 5 seconds. 

\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*

One idea that we came up with is adding a vibration motor to the device in order to give the user some kind of physical feedback along with the light feedback. This way, in case they miss the light feedback, they will still feel the vibration while holding the toothbrush.

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

\*\***Give us feedback on Tinkerbelle.**\*\*

Tinkerbelle was pretty straightforward for me. Since I am on a windows machine, I just downloaded the zip file of the entire project directory and ran the python file using an IDE. Once I ran the file, the server was live as shown in the image below.

![image](https://user-images.githubusercontent.com/70334332/132592669-a2aab86e-fbeb-45bb-b37c-51b89ed1e974.png)

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

\*\***Include your first attempts at recording the set-up video here.**\*\*

My set-up work basically involved setting up Tinkerbelle and making sure that I can use Jane to change the color of my phone screen using my computer. Below is a video showing how that works.

[Watch the video](https://youtu.be/w2GY4OkvF5c)

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

\*\***Include sketches of what your device might look like here.**\*\*

![Design sketch](https://user-images.githubusercontent.com/70334332/133178060-0ead9cd2-fa82-4c97-8ea3-b9eda28cc59c.jpg)

\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*

The design for my toothbrush aims to be sleek, modern and minimalistic to give users a rich and seamless experience. Some design features include
- There will be only one button on the front of the toothbrush to keep things simple - this will allow the user to turn the toothbrush on/off
- The entire bottom body of the toothbrush will have LED lighting so the users don't miss the light.
- The head of the toothbrush will be removable which will allow users to change the bristles when they get old or choose the softness of the bristles.
- The entire toothbrush will be waterproof since it has to be used in environments where water will be around.
- There will be a built in ultra sonic vibrating motor into the body of the toothbrush that will help users to clean their teeth more efficiently through sonic vibrations.

Here are pictures of the costumed device.
![IMG_0182](https://user-images.githubusercontent.com/70334332/133184094-50f73dfd-e24b-400a-a983-049c7d77572d.JPG)
![IMG_0183](https://user-images.githubusercontent.com/70334332/133184106-df5e7546-6e49-40dd-9085-cc47d57e9fe2.JPG)

## Part F. Record

Here is a video of my interaction with the device. [Watch the video](https://youtu.be/MUkoSiG44i0)

Some notes regarding the video
1. I wasn't able to get help to shoot the video because I live alone. Therefore, I shot the video on my desk instead of the bathroom so I could change the lights while simultaenously staging the interaction.
2. According to the design, the light changes every 30 seconds. However, I changed the light in the video in 10-15 seconds to demonstrate the design with a shorter video and not drag the video out too long.

\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

I worked on this idea by myself.


# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

\*\***Summarize feedback from your partners here.**\*\*

Feedback from Victoria Zhang: "Super cool idea. Being able to track how much time I've spent on each quadrant of my teeth and make sure I am brushing long enough would be a game changer"

Feedback from Jeongmin Huh: "Cool idea. Will the toothbrush notify the user if they go over the 2 minutes mark?" | "Storyboard shows that the toothbrush is already lighted red when the user starts brushing their teeth instead of at the 30 second mark"

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative!
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*

My new design for this interactive toothbrush takes into account some feedback from my peers and also some creative thinking in order to allow for a natural interaction with the user. The changes include:
1. The device will vibrate in a peculiar manner at the 30, 60, 90 second interval to give the user some physical feedback in case they miss the light feedback.
2. When the user presses the start button on the toothbrush, the toothbrush will show a solid blue light 5 seconds. Instead of changing the color of the light every 30 seconds, the toothbrush will show the same blue light every 30 seconds to notify the user to switch their quadrant of the mouth.
3. At the 120 second mark, the toothbrush cycle will end and it will automatically turn off. When this happens, the toothbrush and the light will automatically turn off to notify the user that they have brushed for a 2 minute cycle.
4. If the user wishes to brush for longer, they may press the power button again to restart the 2 minute cycle.

The storyboard for my modified interaction is shown below.
![updated storyboard](https://user-images.githubusercontent.com/70334332/133191137-92b1f053-8c6b-4ce1-8840-b3ae9dff9bed.JPG)

The new interaction video is linked here. [Watch the video](https://youtu.be/MUkoSiG44i0)


