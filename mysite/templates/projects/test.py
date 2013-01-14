<div id="screenblocks" class="container-fluid">

<div class="row-fluid">

<div class="span1"></div>
<div class="span2">
<img src="/static/images/Garrick.jpg" width="145" height="227"  alt="Garick" />

</div><!--/span-->

<div class="span6">
<h4> Garrick </h4>
<p>
Garrick is an original short fictional narrative composed by live-action performance captured on high definition (HD) video conveyed with CGI and classical animation. The main goal of the project is to develop photo realistic virtual environments and their integration with live action. The project also covers the development of workflows in both production and post-production for the automation of rendering processes, and pre-visualization.
</p>

</div><!--/span-->
</div>

<br><br>
<div class="row-fluid">

<div class="span2">

</div>

<div class="span8">
<div id="myCarousel" class="carousel slide">
<!-- Carousel items -->
<div class="carousel-inner">
<div class="item active"><img src="{{ compFrames.0 }}" />  </div>
{% for image in compFrames %}
<div class="item"><img src="{{ image }}" /> </div>
{%  endfor %}
</div>
<!-- Carousel nav -->
<a class="carousel-control left" href="#myCarousel" data-slide="prev">&lsaquo;</a>
<a class="carousel-control right" href="#myCarousel" data-slide="next">&rsaquo;</a>
</div>
</div>

</div>
</div>

<br><br><br>
__author__ = 'alberttsoi'
