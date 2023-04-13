# PyMOL-advance: high-level interface from structure data to manuscript-level figures

With the rapid progress of fields like protein structure prediction, 
an increasing number of researchers from different backgrounds require the use of 
[PyMOL](https://pymol.org/2/) for molecular visualization.
To be used in publications, the default visualization output of PyMOL typically requires 
the spatial adjustments, such as rotating and/or zooming the structures, and 
purposeful emphasis including highlighting important parts and hiding the unimportant parts.
Meanwhile, the need for batch visualization has been demonstrated by recent publications in high-impact journals.
However, these adjustments and batch protocols require the involvement of many skilled personnel, are expensive, 
and operate at human speeds, all of which make them worthy of automation.
Based on the original design of PyMOL and as an important supplement, 
we develop a high-level interface in order to generate figures capable of reaching the 
manuscript or even publication standard with configuration or a few codes.
By using our tool, the manual operations can be greatly reduced, 
and the desired image output can be obtained with only configuration or a few lines of code.

<p align="center">
    <img src="https://github.com/BGI-SynBio/PyMOL-advance/blob/main/docs/source/_static/overview.png"/>
</p>


## Installation
You can install it using pip:

```commandline
   pip install PyMOL-advance
```

Or you can also install it from source after install [git](https://git-scm.com/):

```commandline
   git clone https://github.com/BGI-SynBio/PyMOL-advance.git
   cd PyMOL-advance
   pip install -r requirements.txt
   python setup.py install develop --user
```

The tool requires Python version >= 3.7, and some libraries specified 
in the [requirements file](https://github.com/BGI-SynBio/PyMOL-advance/blob/main/requirements.txt).

## Case presentation
Based on three structures with default visualization output 

<table width="100%" align="center", table-layout:fixed>
    <tr>
        <td bgcolor="#FFFFFF" bgcolor="#FFFFFF" align="center">1AY7</td>
        <td bgcolor="#FFFFFF" bgcolor="#FFFFFF" align="center">1F34</td>
        <td bgcolor="#FFFFFF" bgcolor="#FFFFFF" align="center">1YCR</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF">
            <img width="100%" src="https://github.com/BGI-SynBio/PyMOL-advance/blob/main/cases/baseline/1.1AY7.png"/>
        </td>
        <td bgcolor="#FFFFFF">
            <img width="100%" src="https://github.com/BGI-SynBio/PyMOL-advance/blob/main/cases/baseline/1.1F34.png"/>
        </td>
        <td bgcolor="#FFFFFF">
            <img width="100%" src="https://github.com/BGI-SynBio/PyMOL-advance/blob/main/cases/baseline/1.1YCR.png"/>
        </td>
    </tr>
</table>

an ideal manuscript-level figure 

<p align="center">
    <img width="50%" src="https://github.com/BGI-SynBio/PyMOL-advance/blob/main/cases/designed/1.png"/>
</p>

can be [created](https://github.com/BGI-SynBio/PyMOL-advance/blob/main/cases/case_1.py) 
using 55 lines of code, which is similar to Figure 1 in 
[Carles Corbi-Verge's work](https://biosignaling.biomedcentral.com/articles/10.1186/s12964-016-0131-4).

## Customizations and their protocols
At the figure level, we can customize the target publication format during the 
[initialization](https://github.com/BGI-SynBio/PyMOL-advance/blob/main/mola/layouts.py#L355) of the figure.
The supporting figure formats of journal, conference or publisher are:

<table width="100%" align="center", table-layout:fixed>
    <tr>
        <th bgcolor="#FFFFFF" align="center" rowspan="2">target</th>
        <th bgcolor="#FFFFFF" align="center" rowspan="2">font</th>
        <th bgcolor="#FFFFFF" align="center" rowspan="2">math font</th>
        <th bgcolor="#FFFFFF" align="center" rowspan="2">dpi</th>
        <th bgcolor="#FFFFFF" align="center" rowspan="2">columns</th>
        <th colspan="3">width under column occupy (inches)</th>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">1</td>
        <td bgcolor="#FFFFFF" align="center">2</td>
        <td bgcolor="#FFFFFF" align="center">3</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">Nature</td>
        <td bgcolor="#FFFFFF" align="center">Arial</td>
        <td bgcolor="#FFFFFF" align="center" rowspan="10">Linux Libertine<br/>Lucida Calligraphy</th>
        <td bgcolor="#FFFFFF" align="center">300</td>
        <td bgcolor="#FFFFFF" align="center">2</td>
        <td bgcolor="#FFFFFF" align="center">3.54</td>
        <td bgcolor="#FFFFFF" align="center">7.08</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">Science</td>
        <td bgcolor="#FFFFFF" align="center">Helvetica</td>
        <td bgcolor="#FFFFFF" align="center">300</td>
        <td bgcolor="#FFFFFF" align="center">3</td>
        <td bgcolor="#FFFFFF" align="center">2.24</td>
        <td bgcolor="#FFFFFF" align="center">4.76</td>
        <td bgcolor="#FFFFFF" align="center">7.24</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center" rowspan="2">Cell</th>
        <td bgcolor="#FFFFFF" align="center" rowspan="2">Arial</th>
        <td bgcolor="#FFFFFF" align="center" rowspan="2">300</th>
        <td bgcolor="#FFFFFF" align="center">2</td>
        <td bgcolor="#FFFFFF" align="center">3.35</td>
        <td bgcolor="#FFFFFF" align="center">6.85</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">3</td>
        <td bgcolor="#FFFFFF" align="center">2.17</td>
        <td bgcolor="#FFFFFF" align="center">4.49</td>
        <td bgcolor="#FFFFFF" align="center">6.85</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">PNAS</td>
        <td bgcolor="#FFFFFF" align="center">Helvetica</td>
        <td bgcolor="#FFFFFF" align="center">600</td>
        <td bgcolor="#FFFFFF" align="center">2</td>
        <td bgcolor="#FFFFFF" align="center">3.43</td>
        <td bgcolor="#FFFFFF" align="center">7.08</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">ACS</td>
        <td bgcolor="#FFFFFF" align="center">Arial</td>
        <td bgcolor="#FFFFFF" align="center">600</td>
        <td bgcolor="#FFFFFF" align="center">2</td>
        <td bgcolor="#FFFFFF" align="center">3.30</td>
        <td bgcolor="#FFFFFF" align="center">7.00</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">Oxford</td>
        <td bgcolor="#FFFFFF" align="center">Arial</td>
        <td bgcolor="#FFFFFF" align="center">350</td>
        <td bgcolor="#FFFFFF" align="center">2</td>
        <td bgcolor="#FFFFFF" align="center">3.35</td>
        <td bgcolor="#FFFFFF" align="center">6.70</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">PLOS</td>
        <td bgcolor="#FFFFFF" align="center">Arial</td>
        <td bgcolor="#FFFFFF" align="center">300</td>
        <td bgcolor="#FFFFFF" align="center">1</td>
        <td bgcolor="#FFFFFF" align="center">5.20</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">IEEE</td>
        <td bgcolor="#FFFFFF" align="center">Times New Roman</td>
        <td bgcolor="#FFFFFF" align="center">300</td>
        <td bgcolor="#FFFFFF" align="center">2</td>
        <td bgcolor="#FFFFFF" align="center">3.50</td>
        <td bgcolor="#FFFFFF" align="center">7.16</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
    </tr>
    <tr>
        <td bgcolor="#FFFFFF" align="center">ACM</td>
        <td bgcolor="#FFFFFF" align="center">Linux Libertine</td>
        <td bgcolor="#FFFFFF" align="center">300</td>
        <td bgcolor="#FFFFFF" align="center">2</td>
        <td bgcolor="#FFFFFF" align="center">2.50</td>
        <td bgcolor="#FFFFFF" align="center">6.02</td>
        <td bgcolor="#FFFFFF" align="center">-</td>
    </tr>
</table>

## In preparation

## Acknowledgements
This work is funded by 
[Warren L. DeLano Memorial PyMOL Open-Source Fellowship](http://pymol.org/fellowship). 
We thank Dr. Jarrett Johnson from Schrödinger, Inc. for constructive discussions 
on functional design and implementation mode.