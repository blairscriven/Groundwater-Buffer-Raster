# Groundwater Raster Buffer - QGIS Plugin

Expands and interpolates (nearest neighbour) edge values of Water Surface Elevation (WSE) rasters to produce groundwater (GW) buffer rasters. Requires a raster WSE file and vectorized version of the WSE file; see following examples:

<img src="img\WSE_a.png"  width=30% height=30%><img src="img\WSE_c.png"  width=30% height=30%>

*Data Source: FLUD Research Group, 2020, "Water Surface Elevations: Landcover +10% Roughness Scenario", https://doi.org/10.18738/T8/LBWRDQ, Texas Data Repository, V1*

<br>

Below is an example of a 75 metre groundwater buffer raster processed by the plugin using the above WSE:

<img src="img\WSE_b.png"  width=30% height=30%>

## Installation

Currently, you can download the plugin from GitHub as a zip file and then use the 'Install from ZIP' tab in the plugin manager. The plugin was created for QGIS version 3.22.8 and has not been tested on later versions. Once installed, you should see this icon: ![GW_Rast_icon](icon.png) in the 'Plugin' menu.

Alternatively, you can use the[standalone python](https://github.com/blairscriven/Groundwater-Buffer-Raster/tree/main/extra/stand_alone_script.py) script in a PyQGIS environment. You can also use the [QGIS model](https://github.com/blairscriven/Groundwater-Buffer-Raster/tree/main/extra/GroundWater_RasterBuffer.model3) from the browser.

## Issues

You may need to simplify and smooth the WSE vector file for best results; see [the QGIS Manual](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html?highlight=smooth#smooth). Generally, the [Raster to Polygon](https://pro.arcgis.com/en/pro-app/2.8/tool-reference/conversion/raster-to-polygon.htm) tool in ArcGIS Pro creates vector files that work well with the plugin, especially when the 'Simplify Polygons' option is checked.

If you encounter any other issues, please add a ticket to the'[issues](https://github.com/blairscriven/Groundwater-Buffer-Raster/issues)' tab.

## Suggestions

This plugin is new and will be updated to include better features and improve performance. Feel free to send a comment or a suggestion to my e-mail (scrivenblair@gmail.com)