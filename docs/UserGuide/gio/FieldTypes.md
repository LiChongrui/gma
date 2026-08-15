---
title: FieldTypes
date: 2026-08-15
sidebar: true
---
# gma.gio.FieldTypes


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">FieldTypes</span><span style="font-style: italic; color: black;font-size: 130%;">(ftypes = <span style="color:#48566B">None</span>):</span></span>

Field types object for vector data. Create a FeatureDefn object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ftype  = </b> <code style="text-indent: 0">None||listofFieldType</code>. <span style="color:#48566B;">Default = None</span></p><p style="padding-left: 1em;text-indent: 1em;">    If None, create an empty FieldTypes.</p>

---

## Methods 



### add_ftype




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">add_ftype</span><span style="font-style: italic; color: black;font-size: 120%;">(ftype):</span></span>


Add a FieldType to this FieldTypes.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>ftype: </b> <code style="text-indent: 0">FieldType</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The FieldType to add.</p>

---

### set_gtype




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_gtype</span><span style="font-style: italic; color: black;font-size: 120%;">(gtype):</span></span>


Set a geom type to this FieldTypes.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>gtype: </b> <code style="text-indent: 0">int||str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The geom type to set.</p>

---

## Property 



### ftypes


Field names. -> list



---

### names


Field names. -> list



---