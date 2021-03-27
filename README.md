## Tổng quan về Hệ thống Giám sát - Monitoring

Về tổng quan, điều kiện cần và đủ không thể thiếu cho một hệ thống giám sát bao gồm:
* Giám sát trạng thái, tài nguyên
* Thu thập dữ liệu (Dành cho phân tích, báo cáo)
* Đưa ra cảnh báo khi có sự cố

Việc theo dõi, giám sát toàn bộ cơ sở hạ tầng cung cấp nhiều lợi ích cho một doanh nghiệp chứ không riêng bộ phận IT support hay đội ngũ vận hành.

Chúng ta giám sát tổng quan về hệ thống máy chủ, hệ thống mạng và các ứng dụng để biết tình trạng hoạt động của chúng. Những thông tin này giúp ích chúng ta giữ cho hệ thống hoạt động ổn định hoặc đưa ra nhận định, phương án mở rộng nếu nhận thấy cần thiết, đẩy lùi những sự cố có thể xảy ra. [Đọc thêm...](docs/Monitoring_Overview.md)


## Các ghi chép về OMD - Check MK

### Cấu trúc thư mục:

- `docs`: Nơi lưu trữ những bài viết về cài đặt, vận hành OMD
- `images`: Nơi lưu trữ các hình ảnh phục vụ cho các bài viết
- `tools`: Nơi lưu trữ source code của OMD được tải từ trang chủ
- `script`: Lưu trữ các script tự động cài đặt OMD và một số plugin nhóm tự viết

### Nội dung

#### Phần 1: Lý thuyết

- [1. Tổng quan về OMD - Check_MK](https://github.com/meditechopen/meditech-ghichep-omd/blob/master/docs/1.%20OMD%20la%20gi%20va%20tai%20sao%20nen%20dung%20OMD.md)

#### Phần 2: Thực hành

- [1. Hướng dẫn cài đặt](#1) <a name="1"></a>
	- [Ubuntu 14.04](docs/1.3.Setup-OMD-U14.04.md)
	- [Ubuntu 16.04](docs/1.2.Setup-OMD-U16.04.md)
	- [CentOS 7](docs/1.1.Setup-OMD-CentOS7.md)
- [2. Cài đặt Agent trên host cần giám sát](docs/2.Install-agent.md)
- [3. Cấu hình Active Check dịch vụ](docs/3.Active-check.md)
- [4. Đặt ngưỡng cảnh báo cho dịch vụ](docs/4.Set-threshold.md)
- [5.1 Cấu hình gửi mail cảnh báo sử dụng Gmail](docs/5.Send-Noitify.md)
- [5.2 Cấu hình gửi cảnh báo sử dụng Slack](docs/5.3-Send-Noitify_Slack.md)
- [6. Thêm plugin vào OMD](docs/6.Add-plugins.md)
- [7. Distributed Monitoring](docs/7.Distributed.md)
- **Bonus:** 
	- [Quản lý các site trên OMD](docs/Management-OMD.md)
	- [Giám sát dịch vụ RabbitMQ](docs/8.Monitor-RabbitMQ.md)
	- [Giám sát dịch vụ MySQL](docs/9.Monitor-MySQL.md)
	- [Backup/Restore một site trong OMD](docs/10.Backup-site.md)
	- [Giám sát OpenStack](docs/11.2.GiamSat-OpenStack.md)
	- [Cấu hình Cluster cho OMD](docs/12.HA-Cluster-OMD.md)
	
(C) MediTech JSC,. - https://meditech.vn
