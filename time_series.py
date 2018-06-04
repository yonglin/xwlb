
# coding: utf-8

# In[1]:


import pickle
import time
import numpy as np
import re
import jieba
import operator
import matplotlib.pyplot as plt
import pandas as pd
#plt.rcParams['font.sans-serif']=['SimHei']
#plt.rcParams['axes.unicode_minus']=False
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.offline as py
import plotly.graph_objs as go


# In[2]:


py.init_notebook_mode(connected=True)


# In[3]:


ls


# In[4]:


df_xwlb = pd.read_csv('df_xwlb.csv')


# In[5]:


df_xwlb.head(20)


# In[6]:


len(df_xwlb)


# In[7]:


df_xwlb.dropna(inplace=True)


# In[8]:


len(df_xwlb)


# In[9]:


101146 - 98906


# In[10]:


df_xwlb['year_id'] = df_xwlb['date_id'].apply(lambda x: int(x[:4]))


# In[11]:


df_xwlb.head()


# In[12]:


#conut frequency
df_xwlb['jzm'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'江泽民|江总书记|江主席', x)))
df_xwlb['hjt'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'胡锦涛|胡总书记|胡主席', x)))
df_xwlb['xjp'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'习近平|习总书记|习大大|习主席', x)))
df_xwlb['zrj'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'朱镕基|朱总理', x)))
df_xwlb['wjb'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'温家宝|温总理', x)))
df_xwlb['lkq'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'李克强|李总理', x)))
df_xwlb['mks'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'马克思|恩格斯', x)))
df_xwlb['ln'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'列宁', x)))
df_xwlb['mzd'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'毛泽东|毛主席', x)))
df_xwlb['dxp'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'邓小平', x)))


# In[13]:


df_xwlb['shzy'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'社会主义', x)))
df_xwlb['gczy'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'共产主义', x)))
df_xwlb['zbzy'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'资本主义', x)))


# In[14]:


df_xwlb['dgjq'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'大国崛起', x)))
df_xwlb['wdfx'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'伟大复兴', x)))


# In[15]:


df_xwlb['bdt'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'半导体|芯片|处理器|集成电路', x)))
df_xwlb['zzzs'] = df_xwlb['news'].apply(lambda x: len(re.findall(r'自主研发|自主知识产权|国产', x)))


# In[16]:


df_xwlb.head(2)


# In[17]:


grouped_date = df_xwlb.groupby('year_id')


# In[18]:


year_xjp = grouped_date['xjp'].apply(lambda x: x.sum())
year_jzm = grouped_date['jzm'].apply(lambda x: x.sum())
year_hjt = grouped_date['hjt'].apply(lambda x: x.sum())
year_zrj = grouped_date['zrj'].apply(lambda x: x.sum())
year_wjb = grouped_date['wjb'].apply(lambda x: x.sum())
year_lkq = grouped_date['lkq'].apply(lambda x: x.sum())
year_mks = grouped_date['mks'].apply(lambda x: x.sum())
year_ln = grouped_date['ln'].apply(lambda x: x.sum())
year_mzd = grouped_date['mzd'].apply(lambda x: x.sum())
year_dxp = grouped_date['dxp'].apply(lambda x: x.sum())
year_shzy = grouped_date['shzy'].apply(lambda x: x.sum())
year_gczy = grouped_date['gczy'].apply(lambda x: x.sum())
year_zbzy = grouped_date['zbzy'].apply(lambda x: x.sum())
year_dgjq = grouped_date['dgjq'].apply(lambda x: x.sum())
year_wdfx = grouped_date['wdfx'].apply(lambda x: x.sum())
year_bdt= grouped_date['bdt'].apply(lambda x: x.sum())
year_zzzs= grouped_date['zzzs'].apply(lambda x: x.sum())


# In[19]:


type(year_lkq)


# In[20]:


#x_axis = list(df[1:-1].index)
x_axis = year_jzm.index[1:-1]


# In[21]:


year_jzm.index[1:-1]


# In[22]:


#py.sign_in('zhuoylin', 'Y4Rrj8pfHOXq8UsHdx0C')
trace1 = {
  "x": x_axis, 
  "y": year_jzm[1:-1], 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(31, 119, 180)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "江泽民", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "99f6f5", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:237100"
}
trace2 = {
  "x": x_axis, 
  "y": year_hjt[1:-1], 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(255, 127, 14)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "胡锦涛", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "a25197", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:073ed3"
}
trace3 = {
  "x": x_axis, 
  "y": year_xjp[1:-1], 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(44, 160, 44)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "习近平", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "247472", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:cc7c5b"
}
trace4 = {
  "x": x_axis, 
  "y": year_zrj[1:-1], 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(214, 39, 40)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "朱镕基", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "33da55", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:6dc0b2"
}
trace5 = {
  "x": x_axis, 
  "y": year_wjb[1:-1], 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(148, 103, 189)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "温家宝", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "1d107a", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:4e7220"
}
trace6 = {
  "x": x_axis,
  "y": year_lkq[1:-1], 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(140, 86, 75)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "李克强", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:8a3d1d"
}




data = go.Data([trace1, trace2, trace3, trace4, trace5, trace6])
layout = {
  "autosize": False, 
  "font": {"family": "Times New Roman"}, 
  "hovermode": "closest", 
  "paper_bgcolor": "rgb(229, 240, 235)", 
  "title": "<b>2003至2017新闻联播领导人名字出现频率</b>", 
  "titlefont": {
    "family": "Times New Roman", 
    "size": 20
  }, 
  "xaxis": {
    "autorange": True, 
    "nticks": 20, 
    "range": [2002.14147287, 2017.85852713], 
    "ticks": "outside", 
    "title": "<b>年份</b>", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "nticks": 15, 
    "range": [-368.535236396, 5792.5352364], 
    "title": "<b>频率</b>", 
    "type": "linear"
  }
}

#import plotly.graph_objs as go
#fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='xdd.png')


fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[23]:



trace7 = {
  "x": x_axis,
  "y": year_mks[1:-1], 
  "connectgaps": True, 
  "line": {
    "color": "rgb(5, 172, 129)", 
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(10, 10, 10)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines", 
  "name": "马克思", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:358:ee1dc6", 
  "ysrc": "zhuoylin:358:f3694d"
}


trace8 = {
  "x": x_axis,
  "y": year_mzd[1:-1], 
  "connectgaps": True, 
  "line": {
    "color": "rgb(106, 137, 247)", 
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines", 
  "name": "毛泽东", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "d685a3", 
  "xsrc": "zhuoylin:358:ee1dc6", 
  "ysrc": "zhuoylin:358:5b67f0"
}


trace9 = {
  "x": x_axis,
  "y": year_dxp[1:-1], 
  "connectgaps": True, 
  "line": {
    "color": "rgb(214, 39, 40)", 
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(114, 114, 114)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines", 
  "name": "邓小平", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "d79db1", 
  "xsrc": "zhuoylin:358:ee1dc6", 
  "ysrc": "zhuoylin:358:c57922"
}

data_1 = go.Data([trace7,trace8,trace9])
layout_1 = {
  "autosize": False, 
  "font": {"family": "Times New Roman"}, 
  "hovermode": "closest", 
  "paper_bgcolor": "rgb(229, 240, 235)", 
  "title": "<b>2003至2017新闻联播马毛邓出现频率</b>", 
  "titlefont": {
    "family": "Times New Roman", 
    "size": 20
  }, 
  "xaxis": {
    "autorange": True, 
    "nticks": 20, 
    "range": [2002.14147287, 2017.85852713], 
    "ticks": "outside", 
    "title": "<b>年份</b>", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "nticks": 15, 
    "range": [-368.535236396, 5792.5352364], 
    "title": "<b>频率</b>", 
    "type": "linear"
  }
}

#import plotly.graph_objs as go
#fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='xdd.png')


fig_1 = go.Figure(data=data_1, layout=layout_1)
py.iplot(fig_1)


# In[24]:


year_shzy[2018]=year_shzy[2018]*365/139
year_zbzy[2018]=year_zbzy[2018]*365/139
year_gczy[2018]=year_gczy[2018]*365/139


# In[25]:


trace10 = {
  "x": year_shzy.index,
  "y": year_shzy, 
  "connectgaps": True, 
  "line": {
    "color": "rgb(214, 39, 40)", 
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(214, 39, 40)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "社会主义", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:8a3d1d"
}


trace11 = {
  "x": year_gczy.index,
  "y": year_gczy, 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(5, 10, 172)",
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "共产主义", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:8a3d1d"
}


trace12 = {
  "x": year_zbzy.index,
  "y": year_zbzy, 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(190, 190, 190)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "资本主义", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:8a3d1d"
}


data_2 = go.Data([trace10,trace11,trace12])
layout_2 = {
  "autosize": False, 
  "font": {"family": "Times New Roman"}, 
  "hovermode": "closest", 
  "paper_bgcolor": "rgb(229, 240, 235)", 
  "title": "<b>2003至2017新闻联播主义出现频率</b>", 
  "titlefont": {
    "family": "Times New Roman", 
    "size": 20
  }, 
  "xaxis": {
    "autorange": True, 
    "nticks": 20, 
    "range": [2002.14147287, 2017.85852713], 
    "ticks": "outside", 
    "title": "<b>年份</b>", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "nticks": 15, 
    "range": [-368.535236396, 5792.5352364], 
    "title": "<b>频率</b>", 
    "type": "linear"
  }
}

#import plotly.graph_objs as go
#fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='xdd.png')


fig_2 = go.Figure(data=data_2, layout=layout_2)
py.iplot(fig_2)


# In[26]:


trace13 = {
  "x": x_axis,
  "y": year_dgjq[1:-1], 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(5, 10, 172)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "大国崛起", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:8a3d1d"
}


trace14 = {
  "x": x_axis,
  "y": year_wdfx[1:-1], 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(106, 137, 247)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "伟大复兴", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:8a3d1d"
}


data_3 = go.Data([trace13,trace14])
layout_3 = {
  "autosize": False, 
  "font": {"family": "Times New Roman"}, 
  "hovermode": "closest", 
  "paper_bgcolor": "rgb(229, 240, 235)", 
  "title": "<b>2003至2017新闻联播关键词出现频率</b>", 
  "titlefont": {
    "family": "Times New Roman", 
    "size": 20
  }, 
  "xaxis": {
    "autorange": True, 
    "nticks": 20, 
    "range": [2002.14147287, 2017.85852713], 
    "ticks": "outside", 
    "title": "<b>年份</b>", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "nticks": 15, 
    "range": [-368.535236396, 5792.5352364], 
    "title": "<b>频率</b>", 
    "type": "linear"
  }
}

#import plotly.graph_objs as go
#fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='xdd.png')


fig_3 = go.Figure(data=data_3, layout=layout_3)
py.iplot(fig_3)


# In[27]:


year_zzzs[2018]=year_zzzs[2018]*365/139
year_bdt[2018]=year_bdt[2018]*365/139


# In[28]:


trace15 = {
  "x": year_bdt.index,
  "y": year_bdt, 
  "connectgaps": True, 
  "line": {
    "color": "rgb(214, 39, 40)", 
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(214, 39, 40)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "半导体芯片", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:8a3d1d"
}


trace16 = {
  "x": year_zzzs.index,
  "y": year_zzzs, 
  "connectgaps": True, 
  "line": {
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(106, 137, 247)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "自主知识产权", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:343:c8b5cd", 
  "ysrc": "zhuoylin:343:8a3d1d"
}


data_4 = go.Data([trace15,trace16])
layout_4 = {
  "autosize": False, 
  "font": {"family": "Times New Roman"}, 
  "hovermode": "closest", 
  "paper_bgcolor": "rgb(229, 240, 235)", 
  "title": "<b>2003至2017新闻联播技术词汇出现频率</b>", 
  "titlefont": {
    "family": "Times New Roman", 
    "size": 20
  }, 
  "xaxis": {
    "autorange": True, 
    "nticks": 20, 
    "range": [2002.14147287, 2017.85852713], 
    "ticks": "outside", 
    "title": "<b>年份</b>", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "nticks": 15, 
    "range": [-368.535236396, 5792.5352364], 
    "title": "<b>频率</b>", 
    "type": "linear"
  }
}

#import plotly.graph_objs as go
#fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='xdd.png')


fig_4 = go.Figure(data=data_4, layout=layout_4)
py.iplot(fig_4)


# In[29]:


#jieba.add_word('一带一路')
#jieba.add_word('十八大')
#jieba.add_word('十九大')
#jieba.add_word('李克强')
#jieba.add_word('国务院总理')
#jieba.add_word('国务院总理李克强')
#jieba.add_word('中国特色')
#jieba.add_word('习近平新时代中国特色社会主义思想')
#jieba.add_word('十九大')
#jieba.add_word('习近平主席')
#jieba.add_word('习近平总书记')
#jieba.add_word('中国特色')
#jieba.add_word('中共中央政治局常委')
#jieba.add_word('中国人民')
#jieba.add_word('国家主席')
#jieba.add_word('习近平同志')
#jieba.add_word('国家主席习近平')
#jieba.add_word('金砖国家')
#jieba.add_word('脱贫攻坚')


# In[30]:


year_xjp[2018]=year_xjp[2018]*365/139
year_wdfx[2018]=year_wdfx[2018]*365/139


# In[31]:


trace17 = {
  "x": year_wdfx.index, 
  "y": year_wdfx, 
  "connectgaps": True, 
  "line": {
    "color": "rgb(31, 119, 180)", 
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(31, 119, 180)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "伟大复兴", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "687804", 
  "xsrc": "zhuoylin:360:763e56", 
  "yaxis": "y2", 
  "ysrc": "zhuoylin:360:587a84"
}
trace18 = {
  "x": year_xjp.index, 
  "y": year_xjp, 
  "connectgaps": True, 
  "line": {
    "color": "rgb(214, 39, 40)", 
    "shape": "spline", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(214, 39, 40)", 
    "size": 6, 
    "symbol": "y-right-open"
  }, 
  "mode": "lines+markers", 
  "name": "习近平", 
  "opacity": 1, 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "e58ed5", 
  "xsrc": "zhuoylin:360:763e56", 
  "ysrc": "zhuoylin:360:982e69"
}
data_5 = go.Data([trace17, trace18])
layout_5 = {
  "autosize": False, 
  "font": {"family": "Times New Roman"}, 
  "height": 450, 
  "hovermode": "closest", 
  "legend": {"orientation": "h"}, 
  "paper_bgcolor": "rgb(229, 240, 235)", 
  "title": "<b>2003至2017新闻联播习近平和伟大复兴出现频率</b>", 
  "titlefont": {
    "family": "Times New Roman", 
    "size": 20
  }, 
  "width": 700, 
  "xaxis": {
    "autorange": True, 
    "nticks": 20, 
    "range": [2000.97178683, 2019.02821317], 
    "ticks": "outside", 
    "title": "<b>年份</b>", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "nticks": 15, 
    "range": [-451.041401274, 6640.04140127], 
    "title": "<b>习近平</b>", 
    "type": "linear"
  }, 
  "yaxis2": {
    "anchor": "x", 
    "autorange": True, 
    "overlaying": "y", 
    "range": [1.78025477707, 365.219745223], 
    "side": "right", 
    "title": "<b>伟大复兴</b>", 
    "type": "linear"
  }
}
fig_5 = go.Figure(data=data_5, layout=layout_5)
py.iplot(fig_5)


# In[32]:


#py.image.save_as(fig_5, filename='xjp_wdfx.png')


# In[33]:


mytext = re.sub(' ', '', mytext)
mytext = re.sub('央视网', '', mytext)
mytext = re.sub('首次', '', mytext)
mytext = re.sub('近日', '', mytext)
mytext = re.sub('这些', '', mytext)
mytext = re.sub('当天', '', mytext)
mytext = re.sub('项目', '', mytext)
mytext = re.sub('这样', '', mytext)
mytext = re.sub('针对', '', mytext)
mytext = re.sub('情况', '', mytext)
mytext = re.sub('varpara', '', mytext)
mytext = re.sub('count', '', mytext)
mytext = re.sub('每天', '', mytext)
mytext = re.sub('可以', '', mytext)
mytext = re.sub('如果', '', mytext)
mytext = re.sub('各地', '', mytext)
mytext = re.sub('解决', '', mytext)
mytext = re.sub('其他', '', mytext)
mytext = re.sub('此外', '', mytext)
mytext = re.sub('昨天', '', mytext)
mytext = re.sub('进一步', '', mytext)
mytext = re.sub('这个', '', mytext)
mytext = re.sub('不能', '', mytext)
mytext = re.sub('必须', '', mytext)
mytext = re.sub('举行', '', mytext)
mytext = re.sub('根据', '', mytext)
mytext = re.sub('宣布', '', mytext)
mytext = re.sub('促进', '', mytext)
mytext = re.sub('当天', '', mytext)
mytext = re.sub('消息', '', mytext)
mytext = re.sub('新闻', '', mytext)
mytext = re.sub('联播', '', mytext)
mytext = re.sub('以及', '', mytext)
mytext = re.sub('目前', '', mytext)
mytext = re.sub('通过', '', mytext)
mytext = re.sub('进行', '', mytext)
mytext = re.sub('他们', '', mytext)
mytext = re.sub('开展', '', mytext)
mytext = re.sub('今年', '', mytext)
mytext = re.sub('一个', '', mytext)
mytext = re.sub('我们', '', mytext)
mytext = re.sub('包括', '', mytext)
mytext = re.sub('今天', '', mytext)
mytext = re.sub('已经', '', mytext)
mytext = re.sub('同时', '', mytext)
mytext = re.sub('正在', '', mytext)
mytext = re.sub('就是', '', mytext)
mytext = re.sub('成为', '', mytext)
mytext = re.sub('去年', '', mytext)
mytext = re.sub('今日', '', mytext)
mytext = re.sub('由于', '', mytext)
mytext = re.sub('需要', '', mytext)
mytext = re.sub('其中', '', mytext)
mytext = re.sub('自己', '', mytext)
mytext = re.sub('不仅', '', mytext)
mytext = re.sub('当地', '', mytext)
mytext = re.sub('开始', '', mytext)
mytext = re.sub('继续', '', mytext)
mytext = re.sub('进入', '', mytext)


# In[34]:


#https://amueller.github.io/word_cloud/


# In[20]:


mytext_list = mytext.split('xxxxxxxxkkkkkkxxxxxxxxxx')


# In[21]:


len(mytext_list)


# In[22]:


jieba_text = list()


# In[23]:


#结巴分词分别处理不同年份
#mytext = " ".join(jieba.cut(mytext))
for item in mytext_list:
    jieba_text.append(" ".join(jieba.cut(item)))


# In[24]:


from wordcloud import WordCloud

wordcloud_list = list()
for text in jieba_text:
    wordcloud = WordCloud(background_color = "black", #设置背景颜色  
                   #mask = "图片",  #设置背景图片  
                   max_words = 100, #设置最大显示的字数  
                   #stopwords = "", #设置停用词  
                   #设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文） 
                   font_path="simsun.ttf",  
                   width=1600, 
                   height=800, 
                   max_font_size = 250,  #设置字体最大值  
                   random_state = 50, #设置有多少种随机生成状态，即有多少种配色方案  
        )
    wordcloud_list.append(wordcloud.generate(text))


# In[25]:


year = 2013
keywords_list = list()
for item in wordcloud_list:
    keywords_list.append(sorted(item.words_.items(), key=operator.itemgetter(1),reverse=True))
    plt.imshow(item, interpolation='bilinear')
    filename = str(year) + ' Top ' + str(item.max_words) + ' Keyword'
    plt.title(filename)
    plt.axis("off")
    item.to_file(filename + '.jpg')
    year+=1
    plt.show()


# In[26]:


#https://zhuanlan.zhihu.com/p/28954970
#https://github.com/fxsjy/jieba
#https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html


# In[27]:


keywords_list[0][:10]


# In[28]:


keywords_list[1][:10]


# In[29]:


keywords_list[2][:10]


# In[30]:


keywords_list[3][:10]


# In[31]:


keywords_list[4][:10]


# In[32]:


keywords_list[5][:10]

