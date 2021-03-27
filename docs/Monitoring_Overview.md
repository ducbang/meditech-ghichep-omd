### Tổng quan về Giám sát

Về tổng quan, điều kiện cần và đủ không thể thiếu cho một hệ thống giám sát bao gồm:
* Giám sát trạng thái, tài nguyên
* Thu thập dữ liệu (Dành cho phân tích, báo cáo)
* Đưa ra cảnh báo khi có sự cố

Việc theo dõi, giám sát toàn bộ cơ sở hạ tầng cung cấp nhiều lợi ích cho một doanh nghiệp chứ không riêng gì bộ phận IT support hay đội ngũ vận hành.

Chúng ta giám sát tổng quan về hệ thống máy chủ, hệ thống mạng và các ứng dụng để biết tình trạng hoạt động của chúng. Nhưng thông tin này giúp ích chúng ta giữ cho hệ thống hoạt động ổn định hoặc đưa ra nhận định, phương án mở rộng nếu nhận thấy cần thiết, đẩy lùi những sự cố có thể xảy ra.

### Khái niệm `check` trong Monitoring

`Check` là một phần của dịch vụ giám sát. Nó được chạy trên máy chủ để thực hiện việc đo lường, thu thập thông tin về trạng thái, tài nguyên. 

Ví dụ: Để kiểm tra một Web server, chúng ta sẽ mở 1 kết nối TCP và sau đó nhận về kết quả.

#### Các trạng thái

##### Với Host

Có 3 trạng thái sau:
* OK: Giữa host và máy chủ giám sát truyền thông được với nhau (PING)
* DOWN: Bị mất kết nối (PING)
* UNREACHABLE: Không xác định được trạng thái trong TH Parent/Child.

##### Với Service

Có 4 trạng thái sau:
* OK: Dịch vụ đang hoạt động bình thường
* WARNING: Dịch vụ, tài nguyên đạt đến ngưỡng thứ 1. Dịch vụ vẫn chạy.
* CRITICAL: Dịch vụ, tài nguyên đạt đến ngưỡng thứ 2. Dịch vụ vẫn chạy, nhưng phải kiểm tra gấp tránh sự cố xảy ra.
* UNKNOWN: TH do mất plugin. DỊch vụ hoặc plugin không tồn tại.

#### Active checks

Việc `check` xuất phát từ máy chủ giám sát tới các máy chủ khác để lấy trạng thái của host, thông tin về tài nguyên (RAM, DISK, CPU,...) và các ứng dụng đang chạy trên đó được gọi là `active check`.

#### Passive checks

Các host sẽ thu thập lại các thông tin và gửi về máy chủ giám sát theo thời gian định sẵn hay bất cứ khi nào có thay đổi. (NCSA - : Nagios Service Check Acceptor, SNMP-Traps,...)

![Acitve-Passive-checks_NAGIOS](https://docs.admicro.vn/uploads/images/2019/04/02/MuWABHcPqL7a52x4pESxnKwg1WZa9aSp.gif "Acitve-Passive-checks_NAGIOS")

### Các thành phần của check_mk

![check_mk-Architecture](https://docs.admicro.vn/uploads/images/2019/04/03/pulGgyEyaibqkqWMWYd9Bicj3fwKOi6Z.png "check_mk-Architecture")

#### Configuration & Check Engine

Check_mk cung cấp một phương thức cấu hình dễ dàng mà không phải phụ thuộc vào thành phần lõi Giám sát; nó giúp chúng ta cấu hình tự động thay vì phải chỉnh sửa trực tiếp vào các file cấu hình và có thể tự động phát hiện dịch vụ/tài nguyên. Các host sẽ được thu thập các thông tin trong một khoảng thời gian được quy định sẵn. Khi có yêu cầu, thông tin sẽ được gửi về check_mk theo dạng Passive checks.

Ở Nagios, thông tin về host, tài nguyên trên các host sẽ được thu thập theo 1 khoảng thời gian nhất định. Ví dụ, nếu muốn kiểm tra tài nguyên Disk và CPU thì mỗi phút phải kiểm  tra 2 lần (1 lần cho DISK và 1 lần cho CPU). Check_MK hoạt động linh hoạt hơn, 2 thông số trên sẽ được thu thập trong 1 lần check. Điều đó giúp ta tiết kiệm khá nhiều tài nguyên.

#### Livestatus

Livestatus cung cấp một kết nối trực tiếp đến Status Data trên Host hoặc service thông qua một Unix-socket. Ví dụ, ứng dụng Nagvis có thể truy xuất trực tiếp để lấy dữ liệu thông qua một kết nối đơn giản mà không cần dùng đến một thư viện chuyên biệt,

#### Multi-site

Multisite cung cấp giao diện điều khiển trực quan, hỗ trợ giám sát phân tán (Distributed Monitoring). Nó có thể được tích hợp với LDAP để xác thực người dùng,
kết hợp thêm với Nagvis và PNP4Nagios (vẽ biểu đồ, sơ đồ). 

#### WATO

WATO là một công cụ để quản trị check_mk thông qua một trình duyệt, có thể quản trị các host, service thông qua các rule. Thêm vào đó, nó cũng có thể quản lý người dùng, tạo các nhóm người dùng, thêm các role, thời điểm (time period) và kế thừa lại Nagios.

#### Notify

Tính năng cảnh báo của check_mk khá linh hoạt nhưng cũng vô cùng đơn giản cho việc cấu hình. Có thể thiết lập được nhiều hình thức cảnh báo khác nhau và có thể xác định cảnh báo theo từng cá nhân hoặc theo nhóm người nào đó. Ví dụ, ta có thể cấu hình những cảnh báo mang tính thông báo qua email và những thông báo quan trọng có thể được gửi SMS trực tiếp tới người có liên quan. 

#### Bussiness Intelligence

BI là một tính năng để giám sát, 'gom' các thành phần, máy chủ hoặc dịch vụ có liên quan tới nhau. Tổng quan, cách này cung cấp cho ta thấy được tổng quan về tình trạng các thành phần. Nếu một thành phần trong nhóm bị lỗi, ta có thể xác định được ví trí chính xác lỗi đó ở đâu.

#### Mobile

Tính năng này cung cấp giao diện sử dụng tối ưu hóa cho các trình duyệt Mobile có thể truy cập tới Livestatus - Status Data. Tính năng này được kích hoạt sẵn khi cài đặt và tương thích với các thiết bị Mobile.

#### Event Console

Event console là tính năng xử lý Log, SNMP-Traps từ các thiết bị gửi về check_mk. Deamon đó có tên là mkeventd - được dùng để cấu hình và thiết lập các rule phân loại mỗi khi có log được gửi tới. Tình năng này sử dụng sẵn Syslog-Daemon để nhận log từ Port 514.

### Tham khảo
* https://check-mk-documentation.readthedocs.io/en/latest/cmkarchitecture.html
* https://www.cybrary.it/0p3n/basics-check_mk-monitoring-system/
* http://www.hpckp.org/images/conference/2014/hpckp14_omd-intro.pdf
* https://mathias-kettner.com/cms.html
