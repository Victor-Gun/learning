/**
 * 列表过滤去重
 * 
 * list = [
 	{'sid':4, 'checked':1},{'sid':6, 'checked':1},{'sid':3, 'checked':1},{'sid':7, 'checked':0},
 	{'sid':5, 'checked':0},{'sid':3, 'checked':1},{'sid':4, 'checked':1},{'sid':4, 'checked':0},{'sid':6, 'checked':1}]
 * e.g. get_unique_list(list, 'sid', 'sid', 'checked')
 */

function get_unique_list(list, uniqueParam, filterParam) {
	return (cur = 0) || data.sort(function(a, b){return a[uniqueParam]-b[uniqueParam]}).filter(function(v){
		return v[filterParam]==1 && (!cur || v[uniqueParam] != cur) ? (cur = v[uniqueParam]) : 0
	});
}