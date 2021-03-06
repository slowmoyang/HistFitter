
def tablefragment(m,table,signalRegions,skiplist,chanStr,showPercent):
  tableline = ''

  tableline += '''
\\begin{tabular}{l'''

  for region in signalRegions:
    tableline += "c"   
  tableline += '''}
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
{\\bf Uncertainty of channel}                                   ''' 

  for region in signalRegions:
    # tableline += " & " + region + "           "   
    tableline += " & " + region.replace('_','\_') + "           "   

  tableline += ''' \\\\
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
%%'''

  tableline += '''
Total background expectation            '''
  for region in signalRegions:
    tableline += " &  $" + str(("%.2f" %m[region]['nfitted'])) + "$       "
  tableline += '''\\\\
%%'''


  tableline += ''' \\\\
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
%%'''



  tableline += '''
Total statistical $(\\sqrt{N_{\\rm exp}})$             '''
  for region in signalRegions:
    tableline += " & $\\pm " + str(("%.2f" %m[region]['sqrtnfitted'])) + "$       "
  tableline += '''\\\\
%%'''

  tableline += '''
Total background systematic              '''

  for region in signalRegions:
    if m[region]['nfitted'] == 0.0:
      percentage = 0.0
    else:
      percentage = m[region]['totsyserr']/m[region]['nfitted'] * 100.0
    tableline += " & $\\pm " + str(("%.2f" %m[region]['totsyserr'])) + "\ [" + str(("%.2f" %percentage)) + "\\%] $       "

  tableline += '''      \\\\
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
%%''' 


  doAsym=False
  #m_listofkeys = m[signalRegions[0]].keys()
  #m_listofkeys.sort()

  d = m[signalRegions[0]] 

  m_listofkeys = sorted(d.iterkeys(), key=lambda k: d[k], reverse=True)

  for name in m_listofkeys:
    if name not in skiplist:
      printname = name
      printname = printname.replace('syserr_','')
      printname = printname.replace('_','\_')
      for index,region in enumerate(signalRegions):
        if index == 0:
          tableline += "\n" + printname + "      "

        #if m[region][name]==0: continue # skip empty systematics
          
        if not showPercent:
          tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + "$       "
        else:
#          percentage = m[region][name]/m[region]['totsyserr'] * 100.0
          percentage = m[region][name]/m[region]['nfitted'] * 100.0
          if percentage <1:
            tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + "\ [" + str(("%.2f" %percentage)) + "\\%] $       "
          else:
            tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + "\ [" + str(("%.1f" %percentage)) + "\\%] $       "
                    
          
        if index == len(signalRegions)-1:
          tableline += '''\\\\
%%'''


  tableline += '''
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
\\end{tabular}
%%'''
    
  return tableline

