#-*- coding: utf-8 -*-
from django.shortcuts import render
from pymongo import MongoClient
import json
from django.shortcuts import render_to_response
import math
import os
client = MongoClient()
db=client.G5
 #a=list(db.Urcosme3.find({"prodtype":"","age":20},{"proname":1,"_id":0,"score":1,"age":1}))
# b=json.dumps(a, ensure_ascii=False).encode('utf8')

# Create your views here.
# def home1(request):
	# context={
	# "aaa":a
	# }
	# return render(request,"index.html",context)
def home2(request):
		try:
			if request.method == 'POST':
				age=request.POST.get('age','N')
				skin=request.POST.get('skin','N')
				prodtype=request.POST.get('prodtype','N')
				price=request.POST.get('price','N')
				
				
				
				
				if age and skin and prodtype and price =="N":
					b='please select all option'
				else:
				
					if price == "A":
							price1=0
							price2=500
					else:
							price1=0
							price2=200000
					# a=list(db.result.aggregate([
					# {"$match":{"protype":int(prodtype),"skintype":skin,"age_deg":age,"price":{"$gte":price1, "$lte": price2}}},
					 # {"$group":{'_id':"$proid", "score_new" :{"$avg" : "$score_new"}
					   # }},{"$sort":{'score_new': -1}}, { "$limit" : 3 }]))
					a=list(db.resultU2.aggregate([
						{"$match":{"protype":int(prodtype),"skintype":skin,"age_deg":age,"price":{"$gte":price1, "$lte": price2}}},
						{"$group":{'_id':"$proid", "score_new" :{"$avg" : "$score_new"}
					}},{"$sort":{'score_new': -1}}, { "$limit" : 3 }]))
					first=a[0]["_id"]#first place id
					second=a[1]["_id"]#second
					third=a[2]["_id"]#third
					
					first_info_list=list(db.osos2.find({"proid":str(first)},{'proname':"1",'_id':"0",'brand':"1"}).limit(1))
					second_info_list=list(db.osos2.find({"proid":str(second)},{'proname':"1",'_id':"0",'brand':"1"}).limit(1))
					third_info_list=list(db.osos2.find({"proid":str(third)},{'proname':"1",'_id':"0",'brand':"1"}).limit(1))
					
					
					first_w=list(db.resultU2.aggregate([
											{"$match":{"protype":int(prodtype),'proid':first,"skintype":skin,"age_deg":age,"price":{"$gte":price1, "$lte": price2}}},
											 {"$group":{'_id':"$proid", "score_new" :{"$avg" : "$score_new"},\
											 "cloud":{"$push":{"保濕" :{"$sum" : "$A"}
									, "溫和低刺激" :{"$sum" : "$B"}
									, "會回購" :{"$sum" : "$C"}
									, "明亮" :{"$sum" : "$D"}
									, "價格實在" :{"$sum" : "$E"}
									, "不引起過敏" :{"$sum" : "$F"}
									, "好吸收" :{"$sum" : "$G"}
									, "清爽" :{"$sum" : "$H"}
									, "不黏膩" :{"$sum" : "$I"}
									, "服貼" :{"$sum" : "$J"}
									, "滋潤" :{"$sum" : "$K"}
									, "不油膩" :{"$sum" : "$L"}
									, "柔嫩" :{"$sum" : "$M"}
									, "不致痘" :{"$sum" : "$N"}
									, "光滑" :{"$sum" : "$O"}
									, "水亮" :{"$sum" : "$P"}
									, "美白" :{"$sum" : "$Q"}
									, "舒緩" :{"$sum" : "$R"}
									, "氣味適中" :{"$sum" : "$S"}
									, "無負擔" :{"$sum" : "$T"}
									, "彈力" :{"$sum" : "$U"}
									, "不致粉刺" :{"$sum" : "$V"}
									, "修護" :{"$sum" : "$W"}
									, "不緊繃" :{"$sum" : "$X"}
									, "鎮定" :{"$sum" : "$Y"}
									, "用量省" :{"$sum" : "$Z"}
									, "好上手" :{"$sum" : "$AA"}
									, "清新" :{"$sum" : "$AB"}
									, "易沖淨" :{"$sum" : "$AC"}
									, "清涼感" :{"$sum" : "$AD"}
									, "保濕不佳" :{"$sum" : "$AE"}
									, "刺激性強" :{"$sum" : "$AF"}
									, "昂貴" :{"$sum" : "$AG"}
									, "引起過敏" :{"$sum" : "$AH"}
									, "不好吸收" :{"$sum" : "$AI"}
									, "不清爽" :{"$sum" : "$AJ"}
									, "黏膩" :{"$sum" : "$AK"}
									, "油膩" :{"$sum" : "$AL"}
									, "致痘" :{"$sum" : "$AM"}
									, "美白無感" :{"$sum" : "$AN"}
									, "氣味不佳" :{"$sum" : "$AO"}
									, "緊繃" :{"$sum" : "$AP"}
									, "用量大" :{"$sum" : "$AQ"}
									, "不易洗淨" :{"$sum" : "$AR"}
									, "控油" :{"$sum" : "$AS"}
									, "不控油" :{"$sum" : "$AT"}
									, "不泛白" :{"$sum" : "$AU"}
									, "粉刺減少" :{"$sum" : "$AV"}
									, "暗沉" :{"$sum" : "$AW"}
									, "不暗沉" :{"$sum" : "$AX"}
									, "淡化黑眼圈無感" :{"$sum" : "$AY"}
									, "淡化細紋" :{"$sum" : "$AZ"}
									, "淡化細紋無感" :{"$sum" : "$BA"}
									, "防曬佳" :{"$sum" : "$BB"}
									, "防曬差" :{"$sum" : "$BC"}
									, "易推勻" :{"$sum" : "$BD"}
									, "不易推勻" :{"$sum" : "$BE"}
									, "不回購" :{"$sum" : "$BF"}
									, "沒效果" :{"$sum" : "$BG"}}}}},
									{"$unwind": '$cloud'}, 
										{"$group": {
											"_id": "$_id",
											"score_new" :{"$avg" : "$score_new"},
											"保濕": {"$sum": "$cloud.保濕"},
											"溫和低刺激" :{"$sum" : "$cloud.溫和低刺激"},
											 "會回購" :{"$sum" : "$cloud.會回購"},
											  "明亮" :{"$sum" : "$cloud.明亮"},
													"價格實在" :{"$sum" : "$cloud.價格實在"}
									, "不引起過敏" :{"$sum" : "$cloud.不引起過敏"}
									   , "好吸收" :{"$sum" : "$cloud.好吸收"}
									   , "清爽" :{"$sum" : "$cloud.清爽"}
									   , "不黏膩" :{"$sum" : "$cloud.不黏膩"}
									   , "服貼" :{"$sum" : "$cloud.服貼"}
									   , "滋潤" :{"$sum" : "$cloud.滋潤"}
									   , "不油膩" :{"$sum" : "$cloud.不油膩"}
									   , "柔嫩" :{"$sum" : "$cloud.柔嫩"}
									   , "不致痘" :{"$sum" : "$cloud.不致痘"}
									   , "光滑" :{"$sum" : "$cloud.光滑"}
									   , "水亮" :{"$sum" : "$cloud.水亮"}
									   , "美白" :{"$sum" : "$cloud.美白"}
									   , "舒緩" :{"$sum" : "$cloud.舒緩"}
									   , "氣味適中" :{"$sum" : "$cloud.氣味適中"}
									   , "無負擔" :{"$sum" : "$cloud.無負擔"}
									   , "彈力" :{"$sum" : "$cloud.彈力"}
									   , "不致粉刺" :{"$sum" : "$cloud.不致粉刺"}
									   , "修護" :{"$sum" : "$cloud.修護"}
									   , "不緊繃" :{"$sum" : "$cloud.不緊繃"}
									   , "鎮定" :{"$sum" : "$cloud.鎮定"}
									   , "用量省" :{"$sum" : "$cloud.用量省"}
									   , "好上手" :{"$sum" : "$cloud.好上手"}
									   , "清新" :{"$sum" : "$cloud.清新"}
									   , "易沖淨" :{"$sum" : "$cloud.易沖淨"}
									   , "清涼感" :{"$sum" : "$cloud.清涼感"}
									   , "保濕不佳" :{"$sum" : "$cloud.保濕不佳"}
									   , "刺激性強" :{"$sum" : "$cloud.刺激性強"}
									   , "昂貴" :{"$sum" : "$cloud.昂貴"}
									   , "引起過敏" :{"$sum" : "$cloud.引起過敏"}
									   , "不好吸收" :{"$sum" : "$cloud.不好吸收"}
									   , "不清爽" :{"$sum" : "$cloud.不清爽"}
									   , "黏膩" :{"$sum" : "$cloud.黏膩"}
									   , "油膩" :{"$sum" : "$cloud.油膩"}
									   , "致痘" :{"$sum" : "$cloud.致痘"}
									   , "美白無感" :{"$sum" : "$cloud.美白無感"}
									   , "氣味不佳" :{"$sum" : "$cloud.氣味不佳"}
									   , "緊繃" :{"$sum" : "$cloud.緊繃"}
									   , "用量大" :{"$sum" : "$cloud.用量大"}
									   , "不易洗淨" :{"$sum" : "$cloud.不易洗淨"}
									   , "控油" :{"$sum" : "$cloud.控油"}
									   , "不控油" :{"$sum" : "$cloud.不控油"}
									   , "不泛白" :{"$sum" : "$cloud.不泛白"}
									   , "粉刺減少" :{"$sum" : "$cloud.粉刺減少"}
									   , "暗沉" :{"$sum" : "$cloud.暗沉"}
									   , "不暗沉" :{"$sum" : "$cloud.不暗沉"}
									   , "淡化黑眼圈無感" :{"$sum" : "$cloud.淡化黑眼圈無感"}
									   , "淡化細紋" :{"$sum" : "$cloud.淡化細紋"}
									   , "淡化細紋無感" :{"$sum" : "$cloud.淡化細紋無感"}
									   , "防曬佳" :{"$sum" : "$cloud.防曬佳"}
									   , "防曬差" :{"$sum" : "$cloud.防曬差"}
									   , "易推勻" :{"$sum" : "$cloud.易推勻"}
									   , "不易推勻" :{"$sum" : "$cloud.不易推勻"}
									   , "不回購" :{"$sum" : "$cloud.不回購"}
									   , "沒效果" :{"$sum" : "$cloud.沒效果"}}
										},{ "$project" : {"_id":0,"保濕": 1,"溫和低刺激": 1,"會回購": 1,"明亮": 1,"價格實在": 1,"不引起過敏": 1,"好吸收": 1,"清爽": 1,"不黏膩": 1,"服貼": 1,"滋潤": 1,"不油膩": 1,"柔嫩": 1,"不致痘": 1,"光滑": 1,"水亮": 1,"美白": 1,"舒緩": 1,"氣味適中": 1,"無負擔": 1,"彈力": 1,"不致粉刺": 1,"修護": 1,"不緊繃": 1,"鎮定": 1,"用量省": 1,"好上手": 1,"清新": 1,"易沖淨": 1,"清涼感": 1,"保濕不佳": 1,"刺激性強": 1,"昂貴": 1,"引起過敏": 1,"不好吸收": 1,"不清爽": 1,"黏膩": 1,"油膩": 1,"致痘": 1,"美白無感": 1,"氣味不佳": 1,"緊繃": 1,"用量大": 1,"不易洗淨": 1,"控油": 1,"不控油": 1,"不泛白": 1,"粉刺減少": 1,"暗沉": 1,"不暗沉": 1,"淡化黑眼圈無感": 1,"淡化細紋": 1,"淡化細紋無感": 1,"防曬佳": 1,"防曬差": 1,"易推勻": 1,"不易推勻": 1,"不回購": 1,"沒效果": 1}    
														   } ]
															 ))
					second_w=list(db.resultU2.aggregate([
											{"$match":{"protype":int(prodtype),'proid':second,"skintype":skin,"age_deg":age,"price":{"$gte":price1, "$lte": price2}}},
											 {"$group":{'_id':"$proid", "score_new" :{"$avg" : "$score_new"},\
											 "cloud":{"$push":{"保濕" :{"$sum" : "$A"}
									, "溫和低刺激" :{"$sum" : "$B"}
									, "會回購" :{"$sum" : "$C"}
									, "明亮" :{"$sum" : "$D"}
									, "價格實在" :{"$sum" : "$E"}
									, "不引起過敏" :{"$sum" : "$F"}
									, "好吸收" :{"$sum" : "$G"}
									, "清爽" :{"$sum" : "$H"}
									, "不黏膩" :{"$sum" : "$I"}
									, "服貼" :{"$sum" : "$J"}
									, "滋潤" :{"$sum" : "$K"}
									, "不油膩" :{"$sum" : "$L"}
									, "柔嫩" :{"$sum" : "$M"}
									, "不致痘" :{"$sum" : "$N"}
									, "光滑" :{"$sum" : "$O"}
									, "水亮" :{"$sum" : "$P"}
									, "美白" :{"$sum" : "$Q"}
									, "舒緩" :{"$sum" : "$R"}
									, "氣味適中" :{"$sum" : "$S"}
									, "無負擔" :{"$sum" : "$T"}
									, "彈力" :{"$sum" : "$U"}
									, "不致粉刺" :{"$sum" : "$V"}
									, "修護" :{"$sum" : "$W"}
									, "不緊繃" :{"$sum" : "$X"}
									, "鎮定" :{"$sum" : "$Y"}
									, "用量省" :{"$sum" : "$Z"}
									, "好上手" :{"$sum" : "$AA"}
									, "清新" :{"$sum" : "$AB"}
									, "易沖淨" :{"$sum" : "$AC"}
									, "清涼感" :{"$sum" : "$AD"}
									, "保濕不佳" :{"$sum" : "$AE"}
									, "刺激性強" :{"$sum" : "$AF"}
									, "昂貴" :{"$sum" : "$AG"}
									, "引起過敏" :{"$sum" : "$AH"}
									, "不好吸收" :{"$sum" : "$AI"}
									, "不清爽" :{"$sum" : "$AJ"}
									, "黏膩" :{"$sum" : "$AK"}
									, "油膩" :{"$sum" : "$AL"}
									, "致痘" :{"$sum" : "$AM"}
									, "美白無感" :{"$sum" : "$AN"}
									, "氣味不佳" :{"$sum" : "$AO"}
									, "緊繃" :{"$sum" : "$AP"}
									, "用量大" :{"$sum" : "$AQ"}
									, "不易洗淨" :{"$sum" : "$AR"}
									, "控油" :{"$sum" : "$AS"}
									, "不控油" :{"$sum" : "$AT"}
									, "不泛白" :{"$sum" : "$AU"}
									, "粉刺減少" :{"$sum" : "$AV"}
									, "暗沉" :{"$sum" : "$AW"}
									, "不暗沉" :{"$sum" : "$AX"}
									, "淡化黑眼圈無感" :{"$sum" : "$AY"}
									, "淡化細紋" :{"$sum" : "$AZ"}
									, "淡化細紋無感" :{"$sum" : "$BA"}
									, "防曬佳" :{"$sum" : "$BB"}
									, "防曬差" :{"$sum" : "$BC"}
									, "易推勻" :{"$sum" : "$BD"}
									, "不易推勻" :{"$sum" : "$BE"}
									, "不回購" :{"$sum" : "$BF"}
									, "沒效果" :{"$sum" : "$BG"}}}}},
									{"$unwind": '$cloud'}, 
										{"$group": {
											"_id": "$_id",
											"score_new" :{"$avg" : "$score_new"},
											"保濕": {"$sum": "$cloud.保濕"},
											"溫和低刺激" :{"$sum" : "$cloud.溫和低刺激"},
											 "會回購" :{"$sum" : "$cloud.會回購"},
											  "明亮" :{"$sum" : "$cloud.明亮"},
													"價格實在" :{"$sum" : "$cloud.價格實在"}
									, "不引起過敏" :{"$sum" : "$cloud.不引起過敏"}
									   , "好吸收" :{"$sum" : "$cloud.好吸收"}
									   , "清爽" :{"$sum" : "$cloud.清爽"}
									   , "不黏膩" :{"$sum" : "$cloud.不黏膩"}
									   , "服貼" :{"$sum" : "$cloud.服貼"}
									   , "滋潤" :{"$sum" : "$cloud.滋潤"}
									   , "不油膩" :{"$sum" : "$cloud.不油膩"}
									   , "柔嫩" :{"$sum" : "$cloud.柔嫩"}
									   , "不致痘" :{"$sum" : "$cloud.不致痘"}
									   , "光滑" :{"$sum" : "$cloud.光滑"}
									   , "水亮" :{"$sum" : "$cloud.水亮"}
									   , "美白" :{"$sum" : "$cloud.美白"}
									   , "舒緩" :{"$sum" : "$cloud.舒緩"}
									   , "氣味適中" :{"$sum" : "$cloud.氣味適中"}
									   , "無負擔" :{"$sum" : "$cloud.無負擔"}
									   , "彈力" :{"$sum" : "$cloud.彈力"}
									   , "不致粉刺" :{"$sum" : "$cloud.不致粉刺"}
									   , "修護" :{"$sum" : "$cloud.修護"}
									   , "不緊繃" :{"$sum" : "$cloud.不緊繃"}
									   , "鎮定" :{"$sum" : "$cloud.鎮定"}
									   , "用量省" :{"$sum" : "$cloud.用量省"}
									   , "好上手" :{"$sum" : "$cloud.好上手"}
									   , "清新" :{"$sum" : "$cloud.清新"}
									   , "易沖淨" :{"$sum" : "$cloud.易沖淨"}
									   , "清涼感" :{"$sum" : "$cloud.清涼感"}
									   , "保濕不佳" :{"$sum" : "$cloud.保濕不佳"}
									   , "刺激性強" :{"$sum" : "$cloud.刺激性強"}
									   , "昂貴" :{"$sum" : "$cloud.昂貴"}
									   , "引起過敏" :{"$sum" : "$cloud.引起過敏"}
									   , "不好吸收" :{"$sum" : "$cloud.不好吸收"}
									   , "不清爽" :{"$sum" : "$cloud.不清爽"}
									   , "黏膩" :{"$sum" : "$cloud.黏膩"}
									   , "油膩" :{"$sum" : "$cloud.油膩"}
									   , "致痘" :{"$sum" : "$cloud.致痘"}
									   , "美白無感" :{"$sum" : "$cloud.美白無感"}
									   , "氣味不佳" :{"$sum" : "$cloud.氣味不佳"}
									   , "緊繃" :{"$sum" : "$cloud.緊繃"}
									   , "用量大" :{"$sum" : "$cloud.用量大"}
									   , "不易洗淨" :{"$sum" : "$cloud.不易洗淨"}
									   , "控油" :{"$sum" : "$cloud.控油"}
									   , "不控油" :{"$sum" : "$cloud.不控油"}
									   , "不泛白" :{"$sum" : "$cloud.不泛白"}
									   , "粉刺減少" :{"$sum" : "$cloud.粉刺減少"}
									   , "暗沉" :{"$sum" : "$cloud.暗沉"}
									   , "不暗沉" :{"$sum" : "$cloud.不暗沉"}
									   , "淡化黑眼圈無感" :{"$sum" : "$cloud.淡化黑眼圈無感"}
									   , "淡化細紋" :{"$sum" : "$cloud.淡化細紋"}
									   , "淡化細紋無感" :{"$sum" : "$cloud.淡化細紋無感"}
									   , "防曬佳" :{"$sum" : "$cloud.防曬佳"}
									   , "防曬差" :{"$sum" : "$cloud.防曬差"}
									   , "易推勻" :{"$sum" : "$cloud.易推勻"}
									   , "不易推勻" :{"$sum" : "$cloud.不易推勻"}
									   , "不回購" :{"$sum" : "$cloud.不回購"}
									   , "沒效果" :{"$sum" : "$cloud.沒效果"}}
									},{ "$project" : {"_id":0,"保濕": 1,"溫和低刺激": 1,"會回購": 1,"明亮": 1,"價格實在": 1,"不引起過敏": 1,"好吸收": 1,"清爽": 1,"不黏膩": 1,"服貼": 1,"滋潤": 1,"不油膩": 1,"柔嫩": 1,"不致痘": 1,"光滑": 1,"水亮": 1,"美白": 1,"舒緩": 1,"氣味適中": 1,"無負擔": 1,"彈力": 1,"不致粉刺": 1,"修護": 1,"不緊繃": 1,"鎮定": 1,"用量省": 1,"好上手": 1,"清新": 1,"易沖淨": 1,"清涼感": 1,"保濕不佳": 1,"刺激性強": 1,"昂貴": 1,"引起過敏": 1,"不好吸收": 1,"不清爽": 1,"黏膩": 1,"油膩": 1,"致痘": 1,"美白無感": 1,"氣味不佳": 1,"緊繃": 1,"用量大": 1,"不易洗淨": 1,"控油": 1,"不控油": 1,"不泛白": 1,"粉刺減少": 1,"暗沉": 1,"不暗沉": 1,"淡化黑眼圈無感": 1,"淡化細紋": 1,"淡化細紋無感": 1,"防曬佳": 1,"防曬差": 1,"易推勻": 1,"不易推勻": 1,"不回購": 1,"沒效果": 1}
											   
														   } ]
															 ))
					third_w=list(db.resultU2.aggregate([
											{"$match":{"protype":int(prodtype),'proid':third,"skintype":skin,"age_deg":age,"price":{"$gte":price1, "$lte": price2}}},
											 {"$group":{'_id':"$proid", "score_new" :{"$avg" : "$score_new"},\
											 "cloud":{"$push":{"保濕" :{"$sum" : "$A"}, "溫和低刺激" :{"$sum" : "$B"}, "會回購" :{"$sum" : "$C"}, "明亮" :{"$sum" : "$D"}, "價格實在" :{"$sum" : "$E"}, "不引起過敏" :{"$sum" : "$F"}, "好吸收" :{"$sum" : "$G"}, "清爽" :{"$sum" : "$H"}, "不黏膩" :{"$sum" : "$I"}, "服貼" :{"$sum" : "$J"}, "滋潤" :{"$sum" : "$K"}, "不油膩" :{"$sum" : "$L"}, "柔嫩" :{"$sum" : "$M"}, "不致痘" :{"$sum" : "$N"}, "光滑" :{"$sum" : "$O"}, "水亮" :{"$sum" : "$P"}, "美白" :{"$sum" : "$Q"}, "舒緩" :{"$sum" : "$R"}, "氣味適中" :{"$sum" : "$S"}, "無負擔" :{"$sum" : "$T"}, "彈力" :{"$sum" : "$U"}, "不致粉刺" :{"$sum" : "$V"}, "修護" :{"$sum" : "$W"}, "不緊繃" :{"$sum" : "$X"}, "鎮定" :{"$sum" : "$Y"}, "用量省" :{"$sum" : "$Z"}, "好上手" :{"$sum" : "$AA"}, "清新" :{"$sum" : "$AB"}, "易沖淨" :{"$sum" : "$AC"}, "清涼感" :{"$sum" : "$AD"}, "保濕不佳" :{"$sum" : "$AE"}, "刺激性強" :{"$sum" : "$AF"}, "昂貴" :{"$sum" : "$AG"}, "引起過敏" :{"$sum" : "$AH"}, "不好吸收" :{"$sum" : "$AI"}, "不清爽" :{"$sum" : "$AJ"}, "黏膩" :{"$sum" : "$AK"}, "油膩" :{"$sum" : "$AL"}, "致痘" :{"$sum" : "$AM"}, "美白無感" :{"$sum" : "$AN"}, "氣味不佳" :{"$sum" : "$AO"}, "緊繃" :{"$sum" : "$AP"}, "用量大" :{"$sum" : "$AQ"}, "不易洗淨" :{"$sum" : "$AR"}, "控油" :{"$sum" : "$AS"}, "不控油" :{"$sum" : "$AT"}, "不泛白" :{"$sum" : "$AU"}, "粉刺減少" :{"$sum" : "$AV"}, "暗沉" :{"$sum" : "$AW"}, "不暗沉" :{"$sum" : "$AX"}, "淡化黑眼圈無感" :{"$sum" : "$AY"}, "淡化細紋" :{"$sum" : "$AZ"}, "淡化細紋無感" :{"$sum" : "$BA"}, "防曬佳" :{"$sum" : "$BB"}, "防曬差" :{"$sum" : "$BC"}, "易推勻" :{"$sum" : "$BD"}, "不易推勻" :{"$sum" : "$BE"}, "不回購" :{"$sum" : "$BF"}, "沒效果" :{"$sum" : "$BG"}}}}},
									{"$unwind": '$cloud'}, 
										{"$group": {
											"_id": "$_id",
											"score_new" :{"$avg" : "$score_new"},
										   "保濕": {"$sum": "$cloud.保濕"},
											"溫和低刺激" :{"$sum" : "$cloud.溫和低刺激"},
											 "會回購" :{"$sum" : "$cloud.會回購"},
											  "明亮" :{"$sum" : "$cloud.明亮"},
													"價格實在" :{"$sum" : "$cloud.價格實在"}
									, "不引起過敏" :{"$sum" : "$cloud.不引起過敏"}
									   , "好吸收" :{"$sum" : "$cloud.好吸收"}
									   , "清爽" :{"$sum" : "$cloud.清爽"}
									   , "不黏膩" :{"$sum" : "$cloud.不黏膩"}
									   , "服貼" :{"$sum" : "$cloud.服貼"}
									   , "滋潤" :{"$sum" : "$cloud.滋潤"}
									   , "不油膩" :{"$sum" : "$cloud.不油膩"}
									   , "柔嫩" :{"$sum" : "$cloud.柔嫩"}
									   , "不致痘" :{"$sum" : "$cloud.不致痘"}
									   , "光滑" :{"$sum" : "$cloud.光滑"}
									   , "水亮" :{"$sum" : "$cloud.水亮"}
									   , "美白" :{"$sum" : "$cloud.美白"}
									   , "舒緩" :{"$sum" : "$cloud.舒緩"}
									   , "氣味適中" :{"$sum" : "$cloud.氣味適中"}
									   , "無負擔" :{"$sum" : "$cloud.無負擔"}
									   , "彈力" :{"$sum" : "$cloud.彈力"}
									   , "不致粉刺" :{"$sum" : "$cloud.不致粉刺"}
									   , "修護" :{"$sum" : "$cloud.修護"}
									   , "不緊繃" :{"$sum" : "$cloud.不緊繃"}
									   , "鎮定" :{"$sum" : "$cloud.鎮定"}
									   , "用量省" :{"$sum" : "$cloud.用量省"}
									   , "好上手" :{"$sum" : "$cloud.好上手"}
									   , "清新" :{"$sum" : "$cloud.清新"}
									   , "易沖淨" :{"$sum" : "$cloud.易沖淨"}
									   , "清涼感" :{"$sum" : "$cloud.清涼感"}
									   , "保濕不佳" :{"$sum" : "$cloud.保濕不佳"}
									   , "刺激性強" :{"$sum" : "$cloud.刺激性強"}
									   , "昂貴" :{"$sum" : "$cloud.昂貴"}
									   , "引起過敏" :{"$sum" : "$cloud.引起過敏"}
									   , "不好吸收" :{"$sum" : "$cloud.不好吸收"}
									   , "不清爽" :{"$sum" : "$cloud.不清爽"}
									   , "黏膩" :{"$sum" : "$cloud.黏膩"}
									   , "油膩" :{"$sum" : "$cloud.油膩"}
									   , "致痘" :{"$sum" : "$cloud.致痘"}
									   , "美白無感" :{"$sum" : "$cloud.美白無感"}
									   , "氣味不佳" :{"$sum" : "$cloud.氣味不佳"}
									   , "緊繃" :{"$sum" : "$cloud.緊繃"}
									   , "用量大" :{"$sum" : "$cloud.用量大"}
									   , "不易洗淨" :{"$sum" : "$cloud.不易洗淨"}
									   , "控油" :{"$sum" : "$cloud.控油"}
									   , "不控油" :{"$sum" : "$cloud.不控油"}
									   , "不泛白" :{"$sum" : "$cloud.不泛白"}
									   , "粉刺減少" :{"$sum" : "$cloud.粉刺減少"}
									   , "暗沉" :{"$sum" : "$cloud.暗沉"}
									   , "不暗沉" :{"$sum" : "$cloud.不暗沉"}
									   , "淡化黑眼圈無感" :{"$sum" : "$cloud.淡化黑眼圈無感"}
									   , "淡化細紋" :{"$sum" : "$cloud.淡化細紋"}
									   , "淡化細紋無感" :{"$sum" : "$cloud.淡化細紋無感"}
									   , "防曬佳" :{"$sum" : "$cloud.防曬佳"}
									   , "防曬差" :{"$sum" : "$cloud.防曬差"}
									   , "易推勻" :{"$sum" : "$cloud.易推勻"}
									   , "不易推勻" :{"$sum" : "$cloud.不易推勻"}
									   , "不回購" :{"$sum" : "$cloud.不回購"}
									   , "沒效果" :{"$sum" : "$cloud.沒效果"}}},
										 { "$project" : {"_id":0,"保濕": 1,"溫和低刺激": 1,"會回購": 1,"明亮": 1,"價格實在": 1,"不引起過敏": 1,"好吸收": 1,"清爽": 1,"不黏膩": 1,"服貼": 1,"滋潤": 1,"不油膩": 1,"柔嫩": 1,"不致痘": 1,"光滑": 1,"水亮": 1,"美白": 1,"舒緩": 1,"氣味適中": 1,"無負擔": 1,"彈力": 1,"不致粉刺": 1,"修護": 1,"不緊繃": 1,"鎮定": 1,"用量省": 1,"好上手": 1,"清新": 1,"易沖淨": 1,"清涼感": 1,"保濕不佳": 1,"刺激性強": 1,"昂貴": 1,"引起過敏": 1,"不好吸收": 1,"不清爽": 1,"黏膩": 1,"油膩": 1,"致痘": 1,"美白無感": 1,"氣味不佳": 1,"緊繃": 1,"用量大": 1,"不易洗淨": 1,"控油": 1,"不控油": 1,"不泛白": 1,"粉刺減少": 1,"暗沉": 1,"不暗沉": 1,"淡化黑眼圈無感": 1,"淡化細紋": 1,"淡化細紋無感": 1,"防曬佳": 1,"防曬差": 1,"易推勻": 1,"不易推勻": 1,"不回購": 1,"沒效果": 1}}
										]))
					#first_w=json.dumps(first_w, ensure_ascii=False).encode('utf8')
					first_uw=first_w[0]				
					second_uw=second_w[0]				
					third_uw=third_w[0]
					
					first_score=list(db.radar_x.find({"proid":first,"protype":int(prodtype),"skintype":skin,"age_deg":age},{'_id':0,'proid':0,'age_deg':0,'protype': 0,'skintype': 0}))
					
					first_score=first_score[0]
					second_score=list(db.radar_x.find({"proid":second,"protype":int(prodtype),"skintype":skin,"age_deg":age},{'_id':0,'proid':0,'age_deg':0,'protype': 0,'skintype': 0}))
					
					second_score=second_score[0]
					third_score=list(db.radar_x.find({"proid":third,"protype":int(prodtype),"skintype":skin,"age_deg":age},{'_id':0,'proid':0,'age_deg':0,'protype': 0,'skintype': 0}))
					
					third_score=third_score[0]
					price_compare=list(db.price217_1.find({"0":first}))
					price_compare=price_compare[0]
					a1=price_compare["1"]
					a2=price_compare["2"]   	
					a3=price_compare["3"]
					a4=price_compare["4"]
					a5=price_compare["5"]
					a6=price_compare["6"]
					a7=price_compare["7"]
					a8=price_compare["8"]
					a9=price_compare["9"]
					a10=price_compare["10"]
					a11=price_compare["11"]
					a12=price_compare["12"]
					a13=price_compare["13"]
					
					bar=list(db.bar_1.find({}))								
					#first_radar_key=sorted(first_score.keys())
					#first_radar_value=sorted(first_score.values(), key=lambda x:x)
					
					# second_radar_key=sorted(second_score.keys())
					#second_radar_value=sorted(second_score.values(), key=lambda x:x)
					#third_radar_key=sorted(third_score.keys())
					#third_radar_value=sorted(third_score.values(), key=lambda x:x)
					
					# eff_f_a=(first_score["item1"])
					# eff_f_b=(first_score["item2"])
					# eff_f_c=(first_score["item3"])
					# eff_f_d=(first_score["item4"])
					# eff_f_e=(first_score["item5"])
					# _________________________________
					# eff_s_a=(second_score["item1"])
					# eff_s_b=(second_score["item2"])
					# eff_s_c=(second_score["item3"])
					# eff_s_d=(second_score["item4"])
					# eff_s_e=(second_score["item5"])
					#_________________________________
					# eff_t_a=(third_score["item1"])
					# eff_t_b=(third_score["item2"])
					# eff_t_c=(third_score["item3"])
					# eff_t_d=(third_score["item4"])
					# eff_t_e=(third_score["item5"])
		except:
			pass
			#b="500元想買這個產品? 好笑"
					
					# bbb=sorted(first_uw.keys(), key=lambda x:first_uw[x], reverse=True)
					# for first_ra_k in bbb[0:6]:
						# first_ra_k=first_ra_k
						
					# ccc=sorted(first_uw.values(), key=lambda x:x, reverse=True)
					# for first_ra_v in ccc[0:6]:
						# first_ra_v=first_ra_v
					
			
			
		return render(request,"index20160204.html",locals())
	