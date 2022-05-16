#!/usr/bin/env python
# coding: utf-8

# In[401]:


import thinkdsp
import thinkplot
import numpy as np


# In[402]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[403]:


# Fetal Heart Rate 


# In[404]:


fh = thinkdsp.read_wave('Fetal hr 10w.wav')


# In[405]:


fh.make_audio()


# In[406]:


fh.plot(label='Fetal Heart Rate/10w')
thinkplot.config(xlabel='Time (S)', ylabel='Amplitude', ylim=[-1.25, 1.25])


# In[407]:


fh_spec=fh.make_spectrum()
fh_spec.plot(color='red',label='Fetal Heart Rate/10w')
thinkplot.config(xlabel='Frequency (Hz)', xlim=[-20, 1500], ylabel='Amplitude', ylim=[-20, 8000])


# In[408]:


fh_spec.peaks()[:5]


# In[409]:


# Placental Sound


# In[410]:


ps = thinkdsp.read_wave('placental snd.wav')


# In[411]:


ps.make_audio()


# In[412]:


ps.plot(label='Placental Whooshing Sound')
thinkplot.config(xlabel='Time (S)', ylabel='Amplitude', ylim=[-1.25, 1.25])


# In[413]:


ps_spec=ps.make_spectrum()
ps_spec.plot(color='red',label='Placental Whooshing Sound')
thinkplot.config(xlabel='Frequency (Hz)', xlim=[-20, 1500], ylabel='Amplitude', ylim=[-20, 2000])


# In[414]:


ps_spec.peaks()[:5]


# In[415]:


# Fetal Movement


# In[416]:


fm = thinkdsp.read_wave('fetal movement.wav')


# In[417]:


fm.make_audio()


# In[418]:


fm.plot(label='Fetal Movement inside Placenta')
thinkplot.config(xlabel='Time (S)', ylabel='Amplitude', ylim=[-1.25, 1.25])


# In[419]:


fm_spec=fm.make_spectrum()
fm_spec.plot(color='red',label='Fetal Movement Inside Placenta')
thinkplot.config(xlabel='Frequency (Hz)', xlim=[-20, 1500], ylabel='Amplitude', ylim=[-20, 2000])


# In[420]:


fm_spec.peaks()[:5]


# In[421]:


# Fetal Blood Flow


# In[422]:


bf= thinkdsp.read_wave('fetal BF.wav')


# In[423]:


bf.make_audio()


# In[424]:


bf.plot(label='Fetal Blood Flow')
thinkplot.config(xlabel='Time (S)', ylabel='Amplitude', ylim=[-1.25, 1.25])


# In[425]:


bf_spec=bf.make_spectrum()
bf_spec.plot(color='red',label='Fetal Blood Flow')
thinkplot.config(xlabel='Frequency (Hz)', xlim=[-20, 1500], ylabel='Amplitude', ylim=[-20, 3000])


# In[426]:


bf_spec.peaks()[:5]


# In[427]:


# Infant's Firstcry


# In[428]:


ff= thinkdsp.read_wave('baby cry.wav')


# In[429]:


ff.make_audio()


# In[430]:


ff.plot(label='Infant Firstcry')
thinkplot.config(xlabel='Time (S)', ylabel='Amplitude', ylim=[-1.25, 1.25])


# In[431]:


ff_spec=ff.make_spectrum()
ff_spec.plot(color='red',label='Infant Firstcry')
thinkplot.config(xlabel='Frequency (Hz)', xlim=[-20, 1500], ylabel='Amplitude', ylim=[-20, 2000])


# In[432]:


ff_spec.peaks()[:5]

