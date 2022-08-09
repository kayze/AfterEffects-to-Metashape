# AfterEffects-to-Metashape
Script to convert AE tracking to Metashape Markers

How to use the script.

Create a Marker in Metashape on you starting image, and make sure to have as many following images as possible.
Export your markers to an XML file.
Open up the XML and locate your marker under "markers".

		Example:

		<markers next_id="2" next_group_id="0">
			<marker id="1" label="point 1"/>
		
take note of your marker ID to find your marker in the next example


Now a bit further down the document under "frames" look for your camera ID where your pinned marker is "true".

		Example:

		<frames next_id="1">
			<frame id="0">
				<markers>
				 <marker marker_id="1">
					 <location camera_id="180" pinned="true" x="4278" y="2187.5"/>
					 <location camera_id="181" pinned="false" x="2094.91284" y="1827.61914"/>
					 <location camera_id="182" pinned="false" x="2054.31055" y="1838.66858"/>
					 <location camera_id="183" pinned="false" x="2010.97913" y="1850.93604"/>
					 <location camera_id="184" pinned="false" x="1969.91235" y="1862.51746"/>
					 <location camera_id="185" pinned="false" x="1929.823" y="1874.91577"/>
					 
Take a note of your camera_id (180 in our case)
                 
                 
Add your images to Aftereffects and track your point.
Select your tracked keyframes and ctrl + c
Paste the text into input.txt, there is no need to edit anything.


Run the python script by opening a commandprompt and type: python main.py

It will now ask you what the starting camera ID is. In our example it's 180.

When the script is done, open the output.txt file and copy the new lines over to your XML and replace the false markers with your new true markers.
                 
Import your XML back into Metashape.
